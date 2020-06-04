from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.LabelsIndex.as_view(), name='index'),
    path('label/<str:article_id>/', views.LabelNews.as_view(), name='show'),
]
