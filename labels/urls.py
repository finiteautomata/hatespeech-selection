from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('label/<str:article_slug>/', views.LabelNews.as_view(), name='show'),
    path('label/delete_all', views.DeleteMyLabels.as_view(), name="delete_all")
]
