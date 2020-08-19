from django.http import Http404
from django.views import View
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from mongoengine.connection import get_db
from mongoengine import DoesNotExist
from hatespeech_models import Article
from .models import Group

class GroupIndex(LoginRequiredMixin, View):
    def get(self, request):
        if Group.objects.count() == 0:
            raise Http404("No group was created")

        group = Group.objects[0]
        return redirect("groups:show", group_name=group.name)

class GroupView(LoginRequiredMixin, View):
    def get_articles(self, group):
        if group:
            articles = group.articles
            articles = sorted(articles, key=lambda x: x.created_at)
        else:
            articles = Article.objects.order_by('-created_at')

        return articles

    def get(self, request, group_name):
        try:
            group = Group.objects.get(name=group_name)
        except DoesNotExist:
            raise Http404("Grupo no existente")

        articles = self.get_articles(group)
        groups = Group.objects
        return render(request, 'groups/show.html', {
            'labeled_count': 0,
            'current_group': group,
            'groups': groups,
            'articles': articles,
        })
