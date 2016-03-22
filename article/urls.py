from django.conf.urls import include, url, patterns
from django.contrib import admin
from article.models import Article

urlpatterns = [
    url(r'^page/1/$', 'article.views.one'),
    url(r'^page/2/$', 'article.views.temp_tow'),
    url(r'^page/3/$', 'article.views.temp_thre'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/(?P<Article_id>\d+)/$', 'article.views.article1'),
    url(r'^articles/addlike/(?P<Article_id>\d+)/$', 'article.views.addlike'),
    url(r'^articles/addcomment/(?P<Article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^articles/', 'article.views.articles'),
    url(r'^auth/login/', 'article.views.login'),
    url(r'^auth/logout/', 'article.views.logout'),
    url(r'^', 'article.views.startmy'),
]