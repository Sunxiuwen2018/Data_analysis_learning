#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:SunXiuWen
# datetime:2025/01/06
# !/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from peewee import SqliteDatabase, Model, CharField, IntegerField

app = Flask(__name__)
# 设置 secret_key
app.config['SECRET_KEY'] = 'your-secret-key-here'
# 配置数据库 (这里使用 SQLite 作为示例)
db = SqliteDatabase('mydatabase.db')


@app.route('/')
def index():
    return "Hello, Flask Admin!"


class User(Model):
    id = IntegerField(primary_key=True)
    username = CharField(unique=True)
    email = CharField(unique=True)


class Meta:
    database = db


# 初始化数据库并创建表
with db:
    db.create_tables([User])

admin = Admin(app, name='My App', template_mode='bootstrap3')
admin.add_view(ModelView(User))

if __name__ == '__main__':
    app.run(debug=True)
