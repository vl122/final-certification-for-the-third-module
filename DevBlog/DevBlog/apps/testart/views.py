from  django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout 
from django.contrib import messages
from django_tables2 import RequestConfig
from django.http import HttpResponse
import django_tables2 as tables
import tablib

from .forms import *

from .models import *

def index(request):
    return render(request, 'testart/number1.html')

def Views(request):
    table_Article = Article.objects.all()
    table_Comment = Comment.objects.all()
    return render(request, 'testart/number2.html',{'table_Article' : table_Article, 'table_Comment':table_Comment})


class LoginUser(LoginView):
   form_class = LoginUserForm
   template_name = 'testart/login.html'
    
   def get_contex_data(self, *, object_list=None, **kwargs):
      context = super().get_contex_data(**kwargs)
      c_def = self.get_user_context(title="Авторизация")
     
      return dict(list(context.items()) + list(c_def.items()))

def logout_user(request):
    logout(request)
    return redirect('login') 

class ArticleTable(tables.Table):
    class Meta:
        model = Article
        attrs = {'class': 'table table-success table-striped'}
        fields = ['article_title', 'article_text', 'pub_date']
        # article_title = tables.Column(attrs={"tf": {"bgcolor": "red"}})
        # attrs = {'class': 'table table-hover'}

class CommentTable(tables.Table):
    class Meta:
        model = Comment
        attrs = {'class': 'table table-dark table-striped'}
        fields = ['article', 'author_name', 'comment_text','rate','usefulness']

def addarticle(request):
    if request.method == 'POST':
        form = AddPostArticle(request.POST)
        if form.is_valid():
            try:
                Article.objects.create(article_title = form.cleaned_data.get("article_title"), article_text= form.cleaned_data.get("article_text"), pub_date= form.cleaned_data.get("pub_date") )
                messages.add_message(request, messages.INFO, 'Спасибо за вашу статью!')
                return redirect('addarticle')
            except:
                form.add_error(None, 'EROR')
        
    else:   
        table = ArticleTable(Article.objects.all())
        RequestConfig(request).configure(table)
        form = AddPostArticle()
        context= {'form': form }
        return render(request, 'testart/addArticle.html', context)


def table_a(request):
    table_a = ArticleTable(Article.objects.all())
    RequestConfig(request).configure(table_a)
    table_c = CommentTable(Comment.objects.all())
    RequestConfig(request).configure(table_c)
    return render(request, 'testart/number2.html' , {'table_Article': table_a, 'table_Comment':table_c})


def export_articles(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        headers = ('Статья', 'Текст статьи', 'Дата публикации')
        data = []
        data = tablib.Dataset(*data, headers = headers)
        data_articles = Article.objects.filter(pub_date__gte = date)
        for data_article in data_articles:
            pub_a_date = data_article.pub_date
            data.append(("Article" +data_article.article_title, f'{pub_a_date}', data_article.article_text))
        response = HttpResponse(data, content_type ='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=articles.xls"

        return response
    return render(request, 'testart/number2.html')


def export_comments(request):
    if request.method == 'POST':
        name_author = request.POST.get('name_article')
        headers = ('article', 'author_name', 'comment_text')
        data = []
        data = tablib.Dataset(*data, headers = headers)
        data_comments = Comment.objects.filter(author_name = name_author)
        for data_comment in data_comments:

            data.append((f'{data_comment.article}', f'{data_comment.author_name}', f'{data_comment.comment_text}'))
        response = HttpResponse(data, content_type ='application/vnd.ms-excel;charset=utf-8')
        response['Content-Disposition'] = "attachment; filename=articles.xls"

        return response
    return render(request, 'testart/number2.html')