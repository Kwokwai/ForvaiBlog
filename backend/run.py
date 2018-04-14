# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import *
from api.Article import Article, ArticleDetail
from api.Category import Category, CategoryDetail
from api.Tag import Tag, TagDetail
from api.Archive import Archive
from core.wrap import Request

app = Flask(__name__)

CORS(app, supports_credentials=True)
api = Api(app)
app.request_class = Request

api.add_resource(Archive, '/archive')
api.add_resource(Article, '/article')
api.add_resource(ArticleDetail, '/article/<id>')
api.add_resource(Category, '/category')
api.add_resource(CategoryDetail, '/category/<id>')
api.add_resource(Tag, '/tag')
api.add_resource(TagDetail, '/tag/<id>')


if __name__ == '__main__':
    app.run(debug=True)


