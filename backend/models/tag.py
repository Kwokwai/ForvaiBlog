import time
from os import urandom
from binascii import b2a_hex
from core.orm import MongoDBM


class Tag(MongoDBM):

    @classmethod
    def create(cls, data=None):
        if data is None:
            data = {}
        tid = cls.getDataNum() + 1
        data['tid'] = tid
        data['time'] = time.time()
        data['createDate'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return super(Tag, cls).create(data)

    def addArticleModel(self, article):
        articleData = self.get('articleList')
        articleMember = {
            'time': time.time(),
            'createDate': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        }
        if articleData:
            articleData[article.articleid] = articleMember
            self.set('articleList', articleData)
        else:
            self.set('articleList', {
                article.articleid: articleMember
            })
        self.save()

    def delArticleModel(self, article):
        articleData = self.get('articleList')
        try:
            del articleData[article.articleid]
            if articleData:
                self.set('articleList', articleData)
            else:
                self.set('articleList', None)
            self.save()
        except:
            pass

    def getArticleIDList(self):
        articleData = self.get('articleList')
        if articleData:
            return articleData.keys()
        return []

    @property
    def tagId(self):
        return str(self.data['_id'])
