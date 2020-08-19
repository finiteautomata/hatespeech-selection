from django.urls import path

from . import views

app_name = 'articles'

urlpatterns = [
    path('article/<str:article_slug>/', views.ArticleView.as_view(), name='show'),
]
