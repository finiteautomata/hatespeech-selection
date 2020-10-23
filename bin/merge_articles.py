from mongoengine import connect
from hatespeech_models import Tweet, Article
from tqdm.auto import tqdm
import fire

def merge_articles(database="hatespeech-selection"):
    """
    Merges articles with the same name
    """

    client = connect(database)

    print("Viendo si hay alguno con búsqueda vacía")

    empty_pars = Article.objects(first_paragraphs=None)
    for art in tqdm(empty_pars, total=empty_pars.count()):
        if not art.first_paragraphs:
            art.save()


    first_count = Article.objects.count()
    print(f"Tenemos {first_count} artículos")

    users = Article.objects.distinct('user')


    for user in users:
        distinct_titles = Article.objects(user=user).distinct('title')

        total_count = Article.objects(user=user).count()
        print(f"{user:<15} --> {len(distinct_titles):<5} distintos, {total_count} total")

        deleted_articles = 0

        for title in tqdm(list(distinct_titles)):
            articles = Article.objects(title=title, user=user).order_by('created_at')
            count = articles.count()

            if count >= 2:
                first_article = articles[0]
                for art in articles[1:]:
                    first_article.comments += art.comments
                    art.delete()
                    deleted_articles += 1
                first_article.save()

        print(f"Artículos borrados de {user:<15}: {deleted_articles}")

if __name__ == "__main__":
    fire.Fire(merge_articles)
