import time, random
from core.orm import MongoDBM


class Article(MongoDBM):

    @classmethod
    def create(cls, data=None):
        if data is None:
            data = {}
        aid = cls.getDataNum() + 1
        data['aid'] = aid
        data['time'] = time.time()
        data['createDate'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return super(Article, cls).create(data)

    @property
    def articleid(self):
        return str(self.data['_id'])

    def addCategoryModel(self, category):
        cate = {
            'time': time.time(),
            'name': category.get('name', ''),
            'cid': category.get('cid', '')
        }

        cateId = str(category.get('_id'))
        categoryData = {
            cateId: cate
        }

        self.set('category', categoryData)
        self.save()

    def delCategoryModel(self, category):
        categoryData = self.get('category')
        try:
            del categoryData[category.categoryId]
            if categoryData:
                self.set('category', categoryData)
            else:
                self.set('category', None)
            self.save()
        except:
            pass

    def addTagModel(self, tag):
        tagData = self.get('tag')
        tagMember = {
            'time': time.time(),
            'createDate': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),
            'tid': tag.get('tid', ''),
            'name': tag.get('name', ''),
        }
        if tagData:
            tagData[tag.tagId] = tagMember
            self.set('tag', tagData)
        else:
            self.set('tag', {
                tag.tagId: tagMember
            })
        self.save()

    def delTagModel(self, tag):
        tagData = self.get('tag')
        try:
            del tagData[tag.tagId]
            if tagData:
                self.set('tag', tagData)
            else:
                self.set('tag', None)
            self.save()
        except:
            pass

