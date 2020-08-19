from bson import ObjectId
from django.http import Http404
from django.views import View
from django.http import JsonResponse
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
    def get(self, request, group_name):
        try:
            group = Group.objects.no_dereference().get(name=group_name)
        except DoesNotExist:
            raise Http404("Grupo no existente")

        article_ids = [t.id for t in group.articles]
        articles = Article.objects(id__in=article_ids)

        groups = Group.objects.no_dereference()
        return render(request, 'groups/show.html', {
            'labeled_count': 0,
            'current_group': group,
            'groups': groups,
            'articles': articles,
        })

class GroupArticleDeleteView(LoginRequiredMixin, View):
    def delete(self, request, group_name, article_id):
        try:
            group = Group.objects.no_dereference().get(name=group_name)

            erased = Group.objects(name=group_name).no_dereference().update_one(pull__articles=ObjectId(article_id))

            return JsonResponse({"erased": erased}, status=200)
        except (DoesNotExist, StopIteration) as e:
            return JsonResponse({"error": "Grupo o artículo no existente o no perteneciente al grupo"}, status=400)
