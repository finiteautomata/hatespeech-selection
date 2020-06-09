from django.http import Http404
from hatespeech_models import Article

def get_article_or_404(**kwargs):
    try:
        article = Article.objects.get(**kwargs)
        return article
    except DoesNotExist:
        raise Http404("Article does not exist")
