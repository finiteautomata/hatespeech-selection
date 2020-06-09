from django.http import Http404
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from mongoengine.connection import get_db
from mongoengine import DoesNotExist
from hatespeech_models import Article

class ArticleIndexView(LoginRequiredMixin, View):
    def get(self, request):

        articles = Article.objects(selected=True).order_by('created_at').only(
            'created_at',
            'text',
            'id',
            'user',
            'slug',
        )

        return render(request, 'articles/index.html', {
            'labeled_count': 0,
            'left_count': articles.count(),
            'articles': articles,
        })

class ArticleView(LoginRequiredMixin, View):
    def get(self, request, article_slug):
        try:
            article = Article.objects.get(slug=article_slug)
        except DoesNotExist:
            raise Http404("Article does not exist")
        return render(request, 'articles/show.html', {
            "article": article
        })
