from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='index'),
    path('<str:group_name>', views.ArticleIndexView.as_view(), name='index'),

    path('<str:article_slug>/', views.ArticleView.as_view(), name='show'),
]
