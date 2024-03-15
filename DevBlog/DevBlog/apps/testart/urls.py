from django.urls import path

from . import views

urlpatterns = [
    path('',views.Views, name = 'Views'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('logout', views.logout_user, name='logout'),
    path('addarticle', views.addarticle, name = 'addarticle'),
    path('table_a', views.table_a, name = 'table_a'),
    path('export_articles',views.export_articles, name = 'export_articles'),
    path('export_comments',views.export_comments, name = 'export_comments')
    # path('1',views.index, name = 'index')
]