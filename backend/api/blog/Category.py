# -*- coding: utf-8 -*-

from flask import request

from core.wrap import Resource as ApiResource
from core.exceptions import ModelRepeat
from models.article import Article as ArticleModel
from models.category import Category as CategoryModel



class Category(ApiResource):
    __mount__ = 'category'

    def get(self):
        iKwargs = request.data
        if iKwargs.__getstate__() == {}:
            allData = self.allData()
            return allData
        else:
            return self.detailData(iKwargs)


    def post(self):
        iKwargs = request.form.to_dict()
        categorys = CategoryModel.getAllData()
        names = [category['name'] for category in categorys]
        category = CategoryModel()
        if iKwargs['name'] in names:
            raise ModelRepeat(iKwargs['name'])
        data = {
            'name': iKwargs['name'],
            'articleList': {}
        }
        category.create(data)
        return data

    def delete(self):
        iKwargs = request.data.to_dict()
        # category = CategoryModel.find({'mk':iKwargs['mk']})
        category = CategoryModel.mustFindOne(iKwargs["id"])
        articlelist = category.getArticleIDList()
        for artcleId in articlelist:
            article = ArticleModel.mustFindOne(artcleId)
            article.delCategoryModel(category)

        category.delete()
        return {}

    def allData(self):
        categorys = CategoryModel.getAllData()
        list = []
        for category in categorys:
            data = {
                'id': str(category.get('_id', '')),
                'mk': category.get('mk', ''),
                'name': category.get('name', ''),
                'articleList': category.get('articleList', ''),
                'createDate': category.get('createDate', '')
            }
            list.append(data)
        resp = {
            'list': list
        }
        return resp

    def detailData(self, iKwargs):
        category = CategoryModel.find({'mk': iKwargs['mk']})
        articlelist = category.getArticleIDList()
        allList = []
        for articleId in articlelist:
            article = ArticleModel.mustFindOne(articleId)
            articledata = {
                'id': str(article.get('_id', '')),
                'mk': article.get('mk', ''),
                'title': article.get('title', ''),
                'summary': article.get('summary', ''),
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
