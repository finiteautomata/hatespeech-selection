from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='index'),
    path('<str:article_id>/', views.ArticleView.as_view(), name='show'),
]
