# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import *
from api.Article import Article
from api.Category import Category
from api.Tag import Tag
from api.Archive import Archive
from core.wrap import Request, Resource
from core.logger import VaiLogs
from gevent.pywsgi import WSGIServer

import api as apis
import conf
import inspect
import os

# app = Flask(__name__)
app = Flask('app', static_folder=None, template_folder=None)

CORS(app, supports_credentials=True)
# api = Api(app)

app.config['DEBUG'] = True
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.request_class = Request

# api.add_resource(Archive, '/archive')
# api.add_resource(Article, '/article')
# api.add_resource(Category, '/category')
# api.add_resource(Tag, '/tag')



def mount_api():
    modules = [apis]
    for module in modules:
        api = getattr(module, 'api')
        for restAPI in module.__all__:
            restAPI = getattr(module, restAPI)
            for m in [i for i in dir(restAPI) if not i.startswith('_')]:
                restClass = getattr(restAPI, m)
                if not inspect.isclass(restClass) or \
                        not issubclass(restClass, Resource) or \
                                restClass in [Resource]:
                    continue

                endpoint = getattr(restClass, '__mount__', None)
                if endpoint:
                    api.add_resource(restClass, endpoint)
                else:
                    raise RuntimeError('%s.%s not has __mount__ attribute' % (restAPI.__name__, m))

        api.init_app(app)


__current_dir = os.path.dirname(os.path.abspath(__file__))


def run_serve():
    os.chdir(__current_dir)
    mount_api()
    print("runing in", conf.server_host, conf.server_port)
    server = WSGIServer((conf.server_host, conf.server_port), app, log=None, backlog=1024)
    server.serve_forever()

if __name__ == '__main__':
    # app.run(debug=True)
    run_serve()

