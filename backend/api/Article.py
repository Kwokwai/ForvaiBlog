# -*- coding: utf-8 -*-

import time

from flask import request
from core.wrap import Resource as ApiResource

from models.article import Article as ArticleModel
from models.category import Category as CategoryModel
from models.tag import Tag as TagModel


class Article(ApiResource):
    def get(self):
        articles = ArticleModel.getAllData()
        list = []
        for article in articles:
            data = {
                'id': str(article.get('_id', '')),
                'aid': article.get('aid', ''),
                'title': article.get('title', ''),
                'content': article.get('content', ''),
                'summery': article.get('summery', ''),
                'createYear': article.get('createDate', '')[:4],
                'createDate': article.get('createDate', '')[5:10],
                'updateDate': article.get('updateDate', ''),
                'category': article.get('category', ''),
                'tag': article.get('tag', '')
            }
            list.append(data)
        resp = {
            'list': list
        }
        return resp

    def post(self):

        data = {
            'title': request.data['title'],
            'summery': request.data['summery'],
            'content': request.data['content'],
        }
        # 创建一篇新文章
        newarticle = ArticleModel.create(data)
        # 添加文章目录分类 只能一个目录分类
        article = ArticleModel.mustFindOne(str(newarticle.get('_id')))
        category = CategoryModel.mustFindOne(request.data['cateid'])
        category.addArticleModel(article)
        article.addCategoryModel(category)

        # 添加文章tag属性 可以多个tag属性
        # tagList = eval(request.data['taglist'])
        # for tagid in tagList:
        #     tag = TagModel.mustFindOne(tagid)
        #     tag.addArticleModel(article)
        #     article.addTagModel(tag)

        resp = {
            'id': str(article.get('_id', '')),
            'aid': str(article.get('aid', '')),
            'title': article.get('title', ''),
            'summery': article.get('summery', ''),
            'content': article.get('content', ''),
            'category': article.get('category', ''),
            'tag': article.get('tag', ''),
            'createDate': article.get('createDate', ''),
            'updateDate': article.get('updateDate', '')
        }
        return resp

    def put(self):
        updateDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        article = ArticleModel.mustFindOne(request.data['id'])
        article.set('content', request.data['content'])
        article.set('summery', request.data['summery'])
        article.set('updateDate', updateDate)
        article.save()
        data = {
            'title': article.get('title', ''),
            'summery': article.get('summery', ''),
            'content': article.get('content', ''),
            'updateDate': article.get('updateDate', ''),
            'createDate': article.get('createDate', '')
        }
        return data

    def delete(self):
        article = ArticleModel.mustFindOne(request.data['id'])

        categoryId = article.get('category', '').keys()
        for cateId in categoryId:
            category = CategoryModel.mustFindOne(cateId)
            category.delArticleModel(article)

        tagIds = article.get('tag', '').keys()
        for tagId in tagIds:
            tag = TagModel.mustFindOne(tagId)
            tag.delArticleModel(article)

        article.delete()
        return {}


class ArticleDetail(ApiResource):
    def get(self, id):
        article = ArticleModel.find({'aid': int(id)})
        if article.get('updateDate', '') == '':
            updateDate = article.get('createDate', '')[:10]
        else:
            updateDate = article.get('updateDate', '')[:10]
        data = {
            'id': str(article.get('_id', '')),
            'aid': article.get('aid', ''),
            'title': article.get('title', ''),
            'content': article.get('content', ''),
            'summery': article.get('summery', ''),
            'createYear': article.get('createDate', '')[:4],
            'createDate': article.get('createDate', '')[5:10],
            'updateDate': updateDate,
            'category': article.get('category', ''),
            'tag': article.get('tag', '')
        }
        return data

