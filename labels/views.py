import json
from django.http import Http404
from django.views import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import JsonResponse
from hate_labelling.helpers import get_article_or_404
from .models import Label
from mongoengine import DoesNotExist, ValidationError
from hatespeech_models import Article

class LabelsIndex(LoginRequiredMixin, View):

    def next_article_to_label(self):
        return Article.objects[0]

    def get(self, request):
        return render(request, 'labels/index.html', {
            'labeled_count': 0,
            'left_count': Article.objects.count(),
            'next_article': self.next_article_to_label(),
        })

class LabelNews(LoginRequiredMixin, View):

    def get(self, request, article_id):
        article = get_article_or_404(article_id)
        return render(request, 'labels/show.html', {
            'article': article,
        })

    def post(self, request):
        try:
            body = json.loads(request.body)
            return JsonResponse({}, status=200)
        except ValidationError as e:
            return JsonResponse
