from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from mongoengine.connection import get_db
from hatespeech_models import Article
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleIndexView(LoginRequiredMixin, View):
    def get(self, request):

        # View code here...
        return render(request, 'articles/index.html', {
            'labeled_count': 0,
            'left_count': Article.objects.count(),
            'articles': Article.objects[:100]
        })
