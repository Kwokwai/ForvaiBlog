# -*- coding: utf-8 -*-

from flask import request
from models.article import Article as ArticleModel
from core.wrap import Resource as ApiResource
from models.tag import Tag as TagModel


class Tag(ApiResource):
    def get(self):
        tags = TagModel.getAllData()
        list = []
        for tag in tags:
            data = {
                'id': str(tag.get('_id', '')),
                'tid': tag.get('tid', ''),
                'name': tag.get('name', ''),
                'articleList': tag.get('articleList', ''),
                'createDate': tag.get('createDate', '')
            }
            list.append(data)
        resp = {
            'list': list
        }
        return resp

    def post(self):
        tag = TagModel()
        data = {
            'name': request.data['name'],
            'articleList': {}
        }
        tag.create(data)
        return data

    def delete(self):
        tag = TagModel.mustFindOne(request.data['id'])
        articlelist = tag.getArticleIDList()
        for artcleId in articlelist:
            article = ArticleModel.mustFindOne(artcleId)
            article.delCategoryModel(tag)
        tag.delete()
        return {}


class TagDetail(ApiResource):
    def get(self, id):
        tag = TagModel.find({'tid': int(id)})
        articlelist = tag.getArticleIDList()
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
                'updateDate': article.get('updateDate', ''),
                'category': article.get('category', ''),
            }
            allList.append(articledata)
        data = {
            'articlelist': allList,
            'name': tag.get('name', '')
        }
        return data