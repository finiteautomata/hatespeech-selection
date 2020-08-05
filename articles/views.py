from django.http import Http404
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from mongoengine.connection import get_db
from mongoengine import DoesNotExist
from hatespeech_models import Article
from .models import Group

class ArticleIndexView(LoginRequiredMixin, View):

    def get_articles(self, group):
        if group:
            articles = group.articles
            articles = sorted(articles, key=lambda x: x.created_at)
        else:
            articles = Article.objects.order_by('-created_at')

        return articles

    def get(self, request, group_name=None):
        try:
            group = Group.objects.get(name=group_name)
        except DoesNotExist:
            if Group.objects.count() > 0:
                group = Group.objects[0]
            else:
                group = None

        articles = self.get_articles(group)
        groups = Group.objects
        return render(request, 'articles/index.html', {
            'labeled_count': 0,
            'current_group': group,
            'groups': groups,
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
