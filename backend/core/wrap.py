from flask import request, make_response
from flask.views import MethodViewType
from flask.wrappers import Request as BaseRequest
from flask_restful import Resource as BaseResource
from flask_restful import Api as BaseApi
from werkzeug.exceptions import BadRequestKeyError
from werkzeug.wrappers import Response as BaseResponse
from werkzeug.utils import cached_property
from collections import OrderedDict

from core.exceptions import APIException
from core.logger import VaiLogs

import json

class ResourceType(MethodViewType):
    def __new__(cls, name, bases, attrs):
        resource_modules = attrs['__module__'].split('.')[-1]
        name = '%s_%s' % (resource_modules, name)
        return super(ResourceType, cls).__new__(cls, name, bases, attrs)


class Resource(BaseResource, metaclass=ResourceType):
    @classmethod
    def as_view(cls, name, *class_args, **class_kwargs):
        v = cls(*class_args, **class_kwargs)

        def view(*args, **kwargs):
            try:
                rsp = v.dispatch_request(*args, **kwargs)
                if isinstance(rsp, BaseResponse):
                    return rsp
                rsp['code'] = 0
                return rsp
            except APIException as e:
                return e.data
            except BadRequestKeyError as e:
                return {
                    'code': 400,
                    'msg': 'miss key %s' % e.args[0]
                }

        if cls.decorators:
            view.__name__ = name
            view.__module__ = cls.__module__
            for decorator in cls.decorators:
                view = decorator(view)

        view.view_class = cls
        view.__name__ = name
        view.__doc__ = cls.__doc__
        view.__module__ = cls.__module__
        view.methods = cls.methods
        view.provide_automatic_options = False
        view.methods.append('OPTIONS')
        return view

    def dispatch_request(self, *args, **kwargs):
        VaiLogs.info(request.method+" "+request.base_url)
        # custom return options request
        if request.method == 'OPTIONS':
            return {"status": 200}

        meth = getattr(self, request.method.lower(), None)
        if meth is None and request.method == 'HEAD':
            meth = getattr(self, 'get', None)

        # NOTE 使用 flask 的 decorators 进行 endpoint 的装饰
        # for decorator in self.method_decorators:
        #     meth = decorator(meth)

        resp = meth(*args, **kwargs)
        if isinstance(resp, BaseResponse):
            return resp
        return resp


class JsonDict(dict):
    def __init__(self, data):
        dict.__init__(self, data)

    def __getitem__(self, key):
        v = dict.get(self, key, None)
        if not v:
            raise BadRequestKeyError(key)
        return v


class Request(BaseRequest):
    """
    customer app request class

    add 'data' method to get app ambiguous request's data
    """

    @cached_property
    def data(self):
        if self.mimetype == 'application/json' and self.get_data():
            return JsonDict(self.get_json())
        if self.method == 'GET':
            return self.args

        if self.form:
            return self.form
        if self.args:
            return self.args
        return JsonDict({})



def custom_output_json(data, code, headers=None):
    dumped = json.dumps(data) + "\n"
    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp


class Api(BaseApi):
    """
    customer flask-restful api object
    """

    def __init__(self, prefix=None):
        super(Api, self).__init__()
        self.prefix = prefix
        self.representations = OrderedDict([
            ('application/json', custom_output_json)
        ])

    def _init_app(self, app):
        """
        wrap the flask-RESTful Api class to avoid deep error handle stack
        """
        # app.handle_exception = partial(self.error_router, app.handle_exception)
        # app.handle_user_exception = partial(self.error_router, app.handle_user_exception)


        for resource, urls, kwargs in self.resources:
            self._register_view(app, resource, *urls, **kwargs)