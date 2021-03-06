import json
import datetime
from django.http import Http404
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from hate_labelling.helpers import get_article_or_404
from .models import Label
from groups.models import Group
from bson.objectid import ObjectId
from mongoengine import DoesNotExist, ValidationError, NotUniqueError
from hatespeech_models import Article

class DeleteMyLabels(LoginRequiredMixin, View):
    def post(self, request):
        """
        Remove all labels from authenticated user
        """
        Label.objects(user_id=request.user.id).delete()

        return redirect("/groups/")


class LabelNews(LoginRequiredMixin, View):
    def get(self, request, article_slug):
        article = get_article_or_404(slug=article_slug)
        comments = self.get_non_labelled_comments(request.user, article)

        return render(request, 'labels/show.html', {
            'article': article,
            'comments': comments,
        })

    def get_non_labelled_comments(self, user, article):
        return article.comments

    def post(self, request, article_slug):
        article = get_article_or_404(slug=article_slug)
        try:
            body = json.loads(request.body)
            label = Label(
                user_id=request.user.id,
                created_at=datetime.datetime.now(),
                tweet_id=body["tweet_id"],
                profane=bool(int(body["profanity"])),
                hateful=bool(int(body["hateful"])),
            )

            label.save()
            return JsonResponse({}, status=200)
        except (ValidationError, NotUniqueError) as e:
            return JsonResponse({"error": str(e)}, status=400)
        except KeyError as e:
            return JsonResponse({ "error": e.message,
            }, status=400)
