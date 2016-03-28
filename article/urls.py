from django.conf.urls import include, url, patterns
from django.contrib import admin
from article.models import Article
from django.conf import settings
from django.conf.urls import static


urlpatterns = [
    url(r'^temp/1/$', 'article.views.one'),
    url(r'^temp/2/$', 'article.views.temp_tow'),
    url(r'^temp/3/$', 'article.views.temp_thre'),
    url(r'^start/$', 'article.views.startmy', name='startmy'),
    url(r'^articles/(?P<page_number>\d+)/(?P<Article_id>\d+)/$', 'article.views.article1', name='article'),
    url(r'^articles/addlike/(?P<page_number>\d+)/(?P<Article_id>\d+)/$', 'article.views.addlike', name='addlike'),
    url(r'^articles/minlike/(?P<page_number>\d+)/(?P<Article_id>\d+)/$', 'article.views.minlike', name='minlike'),
    url(r'^articles/addcomment/(?P<page_number>\d+)/(?P<Article_id>\d+)/$', 'article.views.addcomment', name='addcomment'),
    #url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/page/(?P<page_number>\d+)/$', 'article.views.articles'),
    url(r'^auth/login/', 'article.views.login'),
    url(r'^auth/logout/', 'article.views.logout'),
    url(r'^auth/register/', 'article.views.register'),
    url(r'^', 'article.views.articles'),
]

#if settings.DEBAG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
