# -*- coding: utf-8 -*-
from django.forms import ModelForm
from article.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['Comments_text']
        #fields - указать обязательно!
