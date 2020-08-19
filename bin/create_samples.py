import fire
import sys
import math
import numpy as np
from copy import deepcopy
sys.path.append(".")
from mongoengine import connect, DoesNotExist
from hatespeech_models import Tweet, Article
from groups.models import Group
import random

def create_group(group_name, articles, num_comments):
    try:
        group = Group.objects.get(name=group_name)
    except DoesNotExist:
        group = Group(name=group_name)

    cloned_articles = [
        clone_and_sample_comments(art, num_comments) for art in articles
    ]

    group.articles = cloned_articles
    group.save()

    return group

def clone_and_sample_comments(article, num_comments):
    new_art = deepcopy(article)
    new_art.id = None
    new_art.comments = random.sample(article.comments, num_comments)
    new_art.dummy = True
    new_art.save()

    return new_art



def create_samples(database, drop_groups=True, drop_articles=True, num_articles=30, min_comments=20):
    """
    Create samples of articles to be labelled

    Arguments:

    database: string
        Name of mongo database

    drop_groups: boolean (default: True)
        Whether to drop existing groups of samples

    num_articles: int (default: 30)
        Number of articles to sample

    min_comments: int (default: 20)
        Minimum number of comments to take it into account
    """
    client = connect(database)
    db = client[database]

    if drop_articles:
        deleted = Article.objects(dummy=True).delete()
        print(f"Dropped {deleted} dummy articles")

    print(f"Number of articles: {Article.objects.count()}")

    groups = Group.objects
    if drop_groups:
        print(f"Dropping {groups.count()} groups")
        Group.objects.delete()
    else:
        print("Not dropping groups ")

    initial_query = {
        f"comments__{min_comments-1}__exists": True,
    }
    articles = Article.objects(**initial_query).as_pymongo()
    print(f"Articles with at least {min_comments}: {articles.count()}\n\n")

    articles = list(articles)

    for article in articles:
        hateful_comments = [c for c in article["comments"] if c["hateful_value"] > 0.5]

        article["num_hateful_comments"] = len(hateful_comments)
        article["avg_hate_value"] = sum(c["hateful_value"] for c in article["comments"]) / len(article["comments"])

    """
    Create random group
    """

    random.seed(2020)
    selected_articles = random.sample(articles, num_articles)

    selected_articles = Article.objects(id__in=[t["_id"] for t in selected_articles]).order_by('created_at')

    group = create_group("Random", selected_articles, min_comments)
    print(f"Created {group.name} group with {len(group.articles)} articles")
    """
    Create hateful articles
    """
    thresholded_articles = {
        k:[art for art in articles if art["avg_hate_value"] > k]

        for k in np.arange(0.05, 0.45, 0.10)
    }
    random.seed(2020)

    for key, hateful_articles in thresholded_articles.items():
        selected_articles = random.sample(hateful_articles, num_articles)
        selected_articles = Article.objects(id__in=[t["_id"] for t in selected_articles]).order_by('created_at')
        group_name = f"Comments {key:.2f}"
        group = create_group(group_name, selected_articles, min_comments)
        print(f"Created {group.name} group with {len(group.articles)} articles")

    """
    Create with seed keywords
    """

    seeds = [
        # Las separo en categorías]
        [ "china"],
        [
            "China", "Cuba", "Cubano", "bolivia",
            "Trump", "judío",
        ],
        [
            "camionero", "agresor", "policía", "ladrón", "reprimir", "represión",
            "juez", "justicia", "penal", "criminal", "delito", "denunciar",
        ],
        [
            "mamá", "género",
            "aborto", "actriz", "conductora", "feminista", "madre",
            "femicidios", "mujer", "trans",
        ],

        [
            "cristina", "macri", "morales", "canosa", "evo",
        ]
    ]

    for i in [19, 29, 39, 59]:
        selected_articles = []
        per_category = math.ceil(num_articles / len(seeds))
        for category in seeds:
            text_query = " ".join(category)

            selected_articles += random.sample(list(Article.objects(**{
                f"comments__{i}__exists": True
            }).search_text(text_query)), per_category)

        selected_articles = sorted(selected_articles, key=lambda x: x.created_at)
        group = create_group(f"Seeds > {i+1} comentarios", selected_articles, min_comments)
        print(f"Created {group.name} group with {len(group.articles)} articles")

    # Create one with all keywords

    text_query = " ".join(kw for cat in seeds for kw in cat)

    selected_articles = list(Article.objects(**{
        f"comments__39__exists": True
    }).search_text(text_query))

    # I order this way because if not mongo is exploding

    selected_articles = sorted(selected_articles, key=lambda x: x.created_at)


    group = Group(name=f"Seeds > 40 no sampling")
    group.articles = selected_articles
    group.save()

    print(f"Created {group.name} group with {len(group.articles)} articles")


if __name__ == "__main__":
    fire.Fire(create_samples)
