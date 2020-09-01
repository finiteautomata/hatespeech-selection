from django.urls import path

from . import views

app_name = 'labels'

urlpatterns = [
    path('', views.NewsSelectionIndex.as_view(), name='show'),
]
