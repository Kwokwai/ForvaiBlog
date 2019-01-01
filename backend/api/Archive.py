# -*- coding: utf-8 -*-

from models.article import Article as ArticleModel
from core.wrap import Resource as ApiResource


class Archive(ApiResource):
    __mount__ = '/archive'

    def get(self):
        articles = ArticleModel.getAllData()
        archive = []
        for article in articles:
            data = {
                'id': str(article.get('_id')),
                'aid': article.get('aid', ''),
                'title': article.get('title', ''),
                'createDate': article.get('createDate', ''),
                'time': article.get('time', '')
            }
            archive.append(data)
        resp = {
            'list': archive
        }
        return resp
