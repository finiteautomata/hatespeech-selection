from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.Index.as_view(), name='show'),
    path('next', views.NextArticle.as_view(), name='next'),
    path('select/<str:article_slug>/', views.LabelArticle.as_view(), name="label"),
]
