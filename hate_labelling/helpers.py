from django.http import Http404
from hatespeech_models import Article

def get_article_or_404(article_id):
    try:
        article = Article.objects.get(id=article_id)
        return article
    except DoesNotExist:
        raise Http404("Article does not exist")
