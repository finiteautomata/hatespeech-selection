from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleIndexView.as_view(), name='index'),
]
