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

class NewsSelectionIndex(LoginRequiredMixin, View):
    def get(self, request):
        """
        Remove all labels from authenticated user
        """

        return render(request, "news_selection/index.html")
