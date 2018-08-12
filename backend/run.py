# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import *
from api.Article import Article
from api.Category import Category
from api.Tag import Tag
from api.Archive import Archive
from core.wrap import Request

app = Flask(__name__)

CORS(app, supports_credentials=True)
api = Api(app)
app.request_class = Request

api.add_resource(Archive, '/archive')
api.add_resource(Article, '/article')
api.add_resource(Category, '/category')
api.add_resource(Tag, '/tag')


if __name__ == '__main__':
    app.run(debug=True)


