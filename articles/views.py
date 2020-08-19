from django.http import Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from mongoengine.connection import get_db
from mongoengine import DoesNotExist
from hatespeech_models import Article


class ArticleView(LoginRequiredMixin, View):
    def get(self, request, article_slug):
        try:
            article = Article.objects.get(slug=article_slug)
        except DoesNotExist:
            raise Http404("Article does not exist")
        return render(request, 'articles/show.html', {
            "article": article
        })
