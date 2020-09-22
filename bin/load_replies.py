import fire
from tqdm.auto import tqdm
from mongoengine import connect
from hatespeech_models import Tweet, Article, Reply



def load_replies(database, drop_replies=True):
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

    if drop_replies:
        deleted = Reply.objects.delete()
        print(f"Dropped {deleted} replies")

    articles = Article.objects(dummy__ne=True)
    for art in tqdm(articles, total=articles.count()):
        for comm in art.comments:
            reply = Reply(
                article=art,
                text=comm.text,
                tweet_id=comm.tweet_id,
                user_id=comm.user_id,
                created_at=comm.created_at,
            )

            reply.save()

if __name__ == "__main__":
    fire.Fire(load_replies)
