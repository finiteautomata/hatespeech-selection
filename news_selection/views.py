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
    Show article and actions to set as interesting or not interesting
    """
    def get(self, request, article_slug):
        article = get_article_or_404(slug=article_slug)

        return render(request, "news_selection/select.html", {
            "article": article
        })

class InterestingArticle(LoginRequiredMixin, View):
    def post(self, request, article_slug):
        article = get_article_or_404(slug=article_slug)

        username = request.user.username
        article.set_as_interesting_to(username)

        return redirect("news_selection:next")

class NotInterestingArticle(LoginRequiredMixin, View):
    def post(self, request, article_slug):
        article = get_article_or_404(slug=article_slug)

        username = request.user.username
        article.set_as_not_interesting_to(username)

        return redirect("news_selection:next")
