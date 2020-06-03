import datetime
from mongoengine import (
    DynamicDocument,
    StringField,
    ObjectIdField,
    ReferenceField,
    ListField,
    DateTimeField,
    LongField,
    BooleanField,
    FloatField,
)
from hatespeech_models import Article

class Label(DynamicDocument):
    # Link to the article
    article_id = ReferenceField(Article)
    # Link to the comment
    tweet_id = LongField(required=True)
    user_id = ObjectIdField(required=True)

    meta = {
        'indexes': [
            'article_id'
        ]
    }
