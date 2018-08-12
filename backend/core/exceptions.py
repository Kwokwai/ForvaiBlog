

class APIException(Exception):
    code = 500

    def __init__(self, msg=''):
        self.msg = msg

    @property
    def data(self):
        return {
            'code': self.code,
            'msg': self.msg
        }


class ModelNotFind(APIException):
    code = 500

    def __init__(self, query):
        self.msg = u"%s 找不到该数据" % repr(query)


class ModelRepeat(APIException):
    code = 600

    def __init__(self, query):
        self.msg = u"%s 已存在" % repr(query)