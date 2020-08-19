from django.urls import path

from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupIndex.as_view(), name="index"),
    path('<str:group_name>', views.GroupView.as_view(), name='show'),
]
