# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import context
from django.http import request
from django.shortcuts import render_to_response, redirect
from article.models import Article,Comments
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm
from django.core.context_processors import csrf
from django.contrib import auth
# Create your views here.
def one(request):
    view = 'one page'
    html = '<html><body>is %s </body></html>' % view
    return HttpResponse(html)
def temp_tow(request):
    view = 'temp_tow'
    t = get_template('myview.html')
    html = t.render(context={'name': view})
    return HttpResponse(html)
def temp_thre(request):
    view = 'temp_thre'
    return render_to_response('myview.html', {'name': view})

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all, 'username': auth.get_user(request).username})
# username добавлен для авторизации пользователя

def article1(request, Article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    #токен для формы
    args['article'] = Article.objects.get(id=Article_id)
    args['comments'] = Comments.objects.filter(Comments_id=Article_id)
    args['form'] = comment_form
    # username добавлен для авторизации пользователя
    args['username'] = auth.get_user(request).username
    return render_to_response('article1.html', args)
    #return render_to_response('article1.html', {'article': Article.objects.get(id=Article_id), 'comments': Comments.objects.filter(Comments_id=Article_id)})

def startmy(request):
    return render_to_response('startmy.html')
def addlike(request, Article_id):
    try:
        article = Article.objects.get(id=Article_id)
        article.Article_like += 1
        article.save()
        #<--для куки файлов, учебное не использовать!!!
        response = redirect('articles/')
        response.set_cookie(Article_id, 'test')
        return response
        #для куки файлов, учебное не использовать!!!-->
    except ObjectDoesNotExist:
        raise Http404
    return redirect('articles/')

def addcomment(request, Article_id):
    if request.POST and ('pause' not in request.session):
        # and ('pause' not in request.session) для добавления комментария только 1 в set_expiry(60) - минуту
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # получить данные из формы
            comment.Comments_id = Article.objects.get(id=Article_id)
            form.save()
            # сохранить изменения в форме
            #<--для сесии учебное
            request.session.set_expiry(60)
            request.session['pause'] = True
            #для сесии учебное-->
    return redirect('articles/%s' % Article_id)
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        # username и password без ' !!!
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = 'пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')