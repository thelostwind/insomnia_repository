from django.db import models

class Article(models.Model):
    id = models.AutoField(primary_key = True)
    article_author = models.ForeignKey(Users,db_column = 'article_autor', verbose_name = '作者')
    article_title = models.CharField(max_length = 120, verbose_name = '标题')


class User(models.Model):

