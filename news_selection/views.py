import json
import datetime
import random
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
        username = request.user.username

        """
        We get one random out of the next 100 (at most) articles
        """
        next_articles = Article.next_articles_to_be_labelled(username)
        num_articles = next_articles.count()

        if num_articles == 0:
            return redirect('news_selection:done')

        to_be_considered = min(next_articles.count(), 100)
        idx = random.randint(0, to_be_considered-1)

        article = next_articles[idx]



        return redirect('news_selection:label', article.slug)

class Done(LoginRequiredMixin, View):
    """
    Done labelling :-)
    """
    def get(self, request):
        username = request.user.username

        labeled_articles = Article.objects(seen_by=username).count()
        interesting_articles = Article.objects(interesting_to=username).count()

        return render(request, "news_selection/done.html", {
            "labeled_articles": labeled_articles,
            "interesting_articles": interesting_articles,
        })



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
