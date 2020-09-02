from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.Index.as_view(), name='show'),
    path('next', views.NextArticle.as_view(), name='next'),
    path('done', views.Done.as_view(), name="done"),
    path('select/<str:article_slug>/', views.LabelArticle.as_view(), name="label"),
    path('select/<str:article_slug>/is_interesting', views.InterestingArticle.as_view(), name="is_interesting"),
    path('select/<str:article_slug>/not_interesting', views.NotInterestingArticle.as_view(), name="not_interesting"),
]
