import pymongo
import time
import re
import conf
from core.exceptions import ModelNotFind
from bson.objectid import ObjectId


db = pymongo.MongoClient(conf.mongo_uri, connect=False, maxPoolSize=5, waitQueueMultiple=10)[conf.mongo_database]


def underscore(word):
    """
            copy from inflection.underscore
    """
    word = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', word)
    word = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', word)
    word = word.replace("-", "_")
    return word.lower()


class MongoMeta(type):
    def __new__(meta, name, bases, attrs):
        if name != 'MongoDBM':
            if 'collection' not in attrs:
                    attrs['collection'] = underscore(name)
            if 'buildQueryFromData' not in attrs:
                def query_from_data(data):
                    return {'_id': data['_id']}

                attrs['buildQueryFromData'] = staticmethod(query_from_data)
        return super(MongoMeta, meta).__new__(meta, name, bases, attrs)


class MongoDBM(object, metaclass=MongoMeta):

    db = db
    NotFindError = ModelNotFind

    def __init__(self, obj=None, query=None, fields=None):
        if isinstance(obj, MongoDBM):
            # 继承自父级的数据
            self.data = data = obj.data
            self._update = obj._update
        else:
            self.data = data = obj
            self._update = {}

        if query:
            data = self.db[self.collection].find_one(query, fields)
            if not data:
                raise self.NotFindError(query)
            self.data = data
        self.query = query
        self.fields = fields

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self._update[key] = value

    @property
    def collection(self):
        raise NotImplementedError("Dont't use MongoDBM instance directly")

    @property
    def id(self):
        return str(self.data['_id'])

    def save(self, upsert=True):

        if self._update:
            rv = self.db[self.collection].update_one(self.query, {'$set': self._update}, upsert=upsert)
            if not (rv.matched_count or rv.upserted_id):
                raise self.NotFindError(self.query)
            elif rv.upserted_id:
                self.data['_id'] = rv.upserted_id

            self._update = {}

    def delete(self):
        return self.db[self.collection].delete_one({'_id': self.data['_id']})

    @classmethod
    def create(cls, data=None):
        if data is None:
            data = {}
        data['time'] = time.time()
        data['createDate'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        data['mk'] = str(time.time()).split('.')[0]
        rv = cls.db[cls.collection].insert_one(data)
        data['_id'] = str(rv.inserted_id)
        return cls(data)

    @staticmethod
    def buildQueryFromData(data):
        raise NotImplementedError("Dont't use MongoDBM instance directly")

    @classmethod
    def getAllData(cls):
        datas = cls.db[cls.collection].find()
        if datas:
            return [data for data in datas]

    @classmethod
    def getDataNum(cls):
        data = cls.db[cls.collection].find().count()
        if data:
            return data

    @classmethod
    def find(cls, query):
        data = cls.db[cls.collection].find_one(query)
        if data:
            return cls(data, query=cls.buildQueryFromData(data))

    @classmethod
    def findOne(cls, id):
        return cls.find({'_id': ObjectId(id)})

    @classmethod
    def mustFindOne(cls, _id):
        model = cls.findOne(_id)
        if model:
            return model
        else:
            raise cls.NotFindError(_id)

    @classmethod
    def updateOne(cls, id, update):
        result = cls.db[cls.collection].update_one({'_id': id}, update)
        return result.matched_count

    @classmethod
    def deleteOne(cls, id):
        result = cls.db[cls.collection].delete_one({'_id': id})
        return result.deleted_count

    @classmethod
    def getDataListFromIDList(cls, idList):
        if idList:
            return cls.db[cls.collection].find({'_id': {'$in': idList}})
        return []

    @classmethod
    def getListFromIDList(cls, idList):
        if idList:
            dataList = cls.db[cls.collection].find({'_id': {'$in': idList}})
            return [cls(data) for data in dataList]
        return []

    def __repr__(self):
        return '%r' % self.data


