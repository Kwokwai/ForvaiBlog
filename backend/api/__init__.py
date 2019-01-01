#-*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import re

from os.path import dirname, abspath, isfile, join

from core.wrap import Api

api = Api(prefix='/blog')

__current_dir = abspath(dirname(__file__))

file_list = os.listdir(__current_dir)
rest_file_list = [m[:-3] for m in file_list if isfile(join(__current_dir, m)) and re.search('^[^_].*\.py$', m)]

__all__ = rest_file_list
