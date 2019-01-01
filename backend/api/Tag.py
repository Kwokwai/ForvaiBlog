# -*- coding: utf-8 -*-

from flask import request
from models.article import Article as ArticleModel
from core.wrap import Resource as ApiResource
from core.logger import VaiLogs

from models.tag import Tag as TagModel


class Tag(ApiResource):
    __mount__ = '/tag'

    def get(self):
        iKwargs = request.data
        if iKwargs.__getstate__() == {}:
            allData = self.allData()
            return allData
        else:
            return self.detailData(iKwargs)

    def post(self):
        iKwargs = request.form.to_dict()
        tag = TagModel()
        # data = {
        #     'name': iKwargs['name'],
        #     'articleList': {}
        # }
        iKwargs["articleList"] = {}
        tag.create(iKwargs)
        return {}

    def delete(self):
        iKwargs = request.data
        tag = TagModel.mustFindOne(iKwargs['id'])
        articlelist = tag.getArticleIDList()
        for artcleId in articlelist:
            article = ArticleModel.mustFindOne(artcleId)
            article.delCategoryModel(tag)
        tag.delete()
        return {}


    def allData(self):
        tags = TagModel.getAllData()
        list = []
        for tag in tags:
            data = {
                'id': str(tag.get('_id', '')),
                'mk': tag.get('mk', ''),
                'name': tag.get('name', ''),
                'articleList': tag.get('articleList', ''),
                'createDate': tag.get('createDate', '')
            }
            list.append(data)
        resp = {
            'list': list
        }
        return resp

    def detailData(self, iKwargs):
        tag = TagModel.find({'mk': iKwargs['mk']})
        articlelist = tag.getArticleIDList()
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
                'updateDate': article.get('updateDate', ''),
                'category': article.get('category', ''),
            }
            allList.append(articledata)
        data = {
            'articlelist': allList,
            'name': tag.get('name', '')
        }
        return data
