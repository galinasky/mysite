# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Article(models.Model):

    class Meta:
        # db_table="title"
        ordering = ["Article_title", "Article_date"]

    Article_title = models.CharField(verbose_name='название', max_length=200)
    Article_text = models.TextField(max_length=400)
    Article_date = models.DateTimeField()
    Article_like = models.IntegerField(verbose_name='понравилось', default=0)

class Comments(models.Model):
    # class Meta:
    # db_table="comments"
    Comments_text = models.CharField(verbose_name='комментарий',max_length=300)
    Comments_id = models.ForeignKey(Article)
# название колонок писать с маленькой буквы
# имя модели(таблицы) с большой буквы
