# -*- coding: utf-8 -*-

from flask import request
from models.article import Article as ArticleModel
from core.wrap import Resource as ApiResource
from models.category import Category as CategoryModel


class Category(ApiResource):

    def get(self):
        categorys = CategoryModel.getAllData()
        list = []
        for category in categorys:
            data = {
                'id': str(category.get('_id', '')),
                'cid': category.get('cid', ''),
                'name': category.get('name', ''),
                'articleList': category.get('articleList', ''),
                'createDate': category.get('createDate', '')
            }
            list.append(data)
        resp = {
            'list': list
        }
        return resp

    def post(self):
        category = CategoryModel()
        data = {
            'name': request.data['name'],
            'articleList': {}
        }
        category.create(data)
        return data

    def delete(self):
        category = CategoryModel.mustFindOne(request.data['id'])
        articlelist = category.getArticleIDList()
        for artcleId in articlelist:
            article = ArticleModel.mustFindOne(artcleId)
            article.delCategoryModel(category)

        category.delete()
        return {}


class CategoryDetail(ApiResource):
    def get(self, id):
        category = CategoryModel.find({'cid': int(id)})
        articlelist = category.getArticleIDList()
        allList = []
        for articleId in articlelist:
            article = ArticleModel.mustFindOne(articleId)
            articledata = {
                'id': str(article.get('_id', '')),
                'aid': article.get('aid', ''),
                'title': article.get('title', ''),
                'summery': article.get('summery', ''),
                'createYear': article.get('createDate', '')[:4],
                'createDate': article.get('createDate', '')[5:10],
                'updateDate': article.get('updateDate', '')[:10],
                'category': article.get('category', ''),
            }
            allList.append(articledata)
        data = {
            'articlelist': allList,
            'name': category.get('name', '')
        }
        return data