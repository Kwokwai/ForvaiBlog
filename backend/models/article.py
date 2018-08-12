import time, random
from core.orm import MongoDBM


class Article(MongoDBM):

    @property
    def articleid(self):
        return str(self.data['_id'])

    def addCategoryModel(self, category):
        cate = {
            'time': time.time(),
            'name': category.get('name', ''),
            'mk': category.get('mk', '')
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
            'mk': tag.get('mk', ''),
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

