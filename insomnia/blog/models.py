#coding=utf-8
#! /usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key = True, unique = True)
    user_login = models.CharField(max_length = 60, unique = True, verbose_name = '登录名')
    user_passwd = models.CharField(max_length = 164, verbose_name = '密码')
    user_nickname = models.CharField(max_length = 50, verbose_name = '昵称')
    def __unicode__(self):
        return u'%s' % (self.user_login)


class Category(models.Model):
    id = models.AutoField(primary_key = True)
    cate_name = models.CharField(max_length = 120, verbose_name = '分类名')
    def __unicode__(self):
        return u'%s' % (self.cate_name)

class Post(models.Model):
    id = models.AutoField(primary_key = True)
    post_author = models.ForeignKey(User, db_column = 'post_author', verbose_name = '作者')
    post_title = models.CharField(max_length = 120, verbose_name = '标题')
    post_timestamp = models.DateTimeField(default = datetime.datetime.now, blank = True)
    post_category = models.ForeignKey(Category, db_column = 'post_category', verbose_name = '分类') 
    post_content = models.TextField(verbose_name = '内容')
    def __unicode__(self):
        return u'%s' % (self.post_title)

class Navigation(models.Model):
    id = models.AutoField(primary_key = True)
    nav_title = models.CharField(max_length = 20, unique = True, verbose_name = "导航名")
    nav_seq = models.PositiveSmallIntegerField(unique = True, verbose_name = "排列序号")
    def __unicode__(self):
        return u'%s' % (self.nav_title)

class Comments(models.Model):
    id = models.AutoField(primary_key = True)
    comment_post = models.ForeignKey(Post, db_column = 'comment_post', verbose_name = '文章')
    comment_author = models.CharField(max_length = 100, verbose_name = '评论者')
    comment_date = models.DateTimeField(default=datetime.datetime.now, blank = True, verbose_name='评论日期')
    comment_content = models.TextField(verbose_name = '评论内容')
    def __unicode__(self):
        return u'%s' % (self.comment_content)

class Info(object):
    def get_head_info(self):
        class HeadInfo:
            def __init__(self, blogname, blogdescription, title="Insomnia"):
                self.blogname = blogname
                self.blogdescription = blogdescription
                self.title = title

        blogname = "因索弥亚"
        blogdescription = "你也睡不着吗？"

        info = HeadInfo(blogname, blogdescription)
        return info


