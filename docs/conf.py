#!/usr/bin/env python
# -*- coding:utf-8 -*-
# datetime:2025/01/06
import os
import sys

sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Data_analysis_learning'
copyright = '2025, Mr Sun'
author = 'Mr Sun'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',  # 自动生成 API 文档
    'sphinx.ext.napoleon',  # 支持 Google 和 NumPy 风格的 docstring
    'sphinx.ext.viewcode',  # 显示源代码链接
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'  # 使用 Alabaster 主题
html_static_path = ['_static']
