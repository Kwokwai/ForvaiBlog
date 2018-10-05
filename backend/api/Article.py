# -*- coding: utf-8 -*-

import time, json

from flask import request
from core.wrap import Resource as ApiResource
from core.logger import VaiLogs

from models.article import Article as ArticleModel
from models.category import Category as CategoryModel
from models.tag import Tag as TagModel


class Article(ApiResource):
    def get(self):
        iKwargs = request.data
        if iKwargs.__getstate__() == {}:
            allData = self.allData()
            return allData
        else:
            return self.detailData(iKwargs)

    def post(self):
        iKwargs = request.form.to_dict()
        VaiLogs.info(iKwargs)
        # 创建一篇新文章
        newarticle = ArticleModel.create(iKwargs)
        # 添加文章目录分类 只能一个目录分类
        article = ArticleModel.mustFindOne(str(newarticle.get('_id')))
        if 'cateid' in iKwargs:
            category = CategoryModel.mustFindOne(iKwargs['cateid'])
            category.addArticleModel(article)
            article.addCategoryModel(category)

        # 添加文章tag属性 可以多个tag属性
        if 'taglist' in iKwargs:
            tagList = eval(iKwargs['taglist'])
            for tagid in tagList:
                tag = TagModel.mustFindOne(tagid)
                tag.addArticleModel(article)
                article.addTagModel(tag)

        resp = {
            'id': str(article.get('_id', '')),
            'mk': str(article.get('mk', '')),
            'title': article.get('title', ''),
            'summary': article.get('summary', ''),
            'content': article.get('content', ''),
            'category': article.get('category', ''),
            'tag': article.get('tag', ''),
            'createDate': article.get('createDate', ''),
            'updateDate': article.get('updateDate', '')
        }
        return resp

    def put(self):
        iKwargs = request.form.to_dict()
        updateDate = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        article = ArticleModel.find({'mk':iKwargs['mk']})

        def exit(args):
            if args in iKwargs:
                article.set(args, iKwargs[args])
        exit('content')
        exit('summary')
        exit('title')
        article.set('updateDate', updateDate)
        article.save()
        data = {
            'title': article.get('title', ''),
            'summary': article.get('summary', ''),
            'content': article.get('content', ''),
            'updateDate': article.get('updateDate', ''),
            'createDate': article.get('createDate', ''),
            'mk': article.get('mk', '')
        }
        return data

    def delete(self):
        iKwargs = request.data
        article = ArticleModel.mustFindOne(iKwargs['id'])

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

    # 查询所有数据
    def allData(self):
        articles = ArticleModel.getAllData()
        list = []
        for article in articles:
            data = {
                'id': str(article.get('_id', '')),
                'mk': article.get('mk', ''),
                'title': article.get('title', ''),
                'content': article.get('content', ''),
                'summary': article.get('summary', ''),
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

    # 查询详情数据
    def detailData(self, iKwargs):
        article = ArticleModel.find({'mk': iKwargs['mk']})
        if article.get('updateDate', '') == '':
            updateDate = article.get('createDate', '')[:10]
        else:
            updateDate = article.get('updateDate', '')[:10]
        data = {
            'id': str(article.get('_id', '')),
            'mk': article.get('mk', ''),
            'title': article.get('title', ''),
            'content': article.get('content', ''),
            'summary': article.get('summary', ''),
            'createYear': article.get('createDate', '')[:4],
            'createDate': article.get('createDate', '')[5:10],
            'updateDate': updateDate,
            'category': article.get('category', ''),
            'tag': article.get('tag', '')
        }
        return data



