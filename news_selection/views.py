import json
import datetime
from django.http import Http404
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from hate_labelling.helpers import get_article_or_404
from groups.models import Group
from bson.objectid import ObjectId
from mongoengine import DoesNotExist, ValidationError, NotUniqueError
from hatespeech_models import Article

class Index(LoginRequiredMixin, View):
    def get(self, request):
        """
        Remove all labels from authenticated user
        """

        return render(request, "news_selection/index.html")

class NextArticle(LoginRequiredMixin, View):
    """
    Redirects to next article selection
    """
    def get(self, request):

        # TODO: CHANGE THIS
        article = Article.objects[0]

        return redirect('news_selection:label', article.slug)


class LabelArticle(LoginRequiredMixin, View):
    """
    Redirects to next article selection
    """
    def get(self, request, article_slug):

        # TODO: CHANGE THIS
        article = Article.objects[0]

        return render(request, "news_selection/select.html", {
            "article": article
        })
