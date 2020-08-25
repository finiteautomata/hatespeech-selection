import json
from django.http import Http404, HttpResponseForbidden
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from mongoengine.connection import get_db
from mongoengine import DoesNotExist
from groups.models import Group
from hatespeech_models import Article


class ArticleView(LoginRequiredMixin, View):
    def get(self, request, article_slug):

        """
        Let's check out if there is a group

        """
        try:
            group = Group.objects.no_dereference().get(name=request.GET['group'])
        except (MultiValueDictKeyError, DoesNotExist) as e:
            group = None

        try:
            article = Article.objects.get(slug=article_slug)
        except DoesNotExist:
            raise Http404("Article does not exist")
        return render(request, 'articles/show.html', {
            "article": article,
            "group": group,
        })

    def put(self, request, article_slug):
        if not request.user.is_superuser:
            raise HttpResponseForbidden()

        try:
            article = Article.objects.get(slug=article_slug)
        except DoesNotExist:
            raise Http404("Article does not exist")

        # awful
        arguments = json.loads(request.body.decode("utf-8"))

        """
        TODO: modify this
        """
        article.description = arguments["description"]

        article.save()

        return JsonResponse({}, status=200)
