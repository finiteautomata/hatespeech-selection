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
    # Link to the comment
    tweet_id = LongField(required=True, unique_with="user_id")
    hateful = BooleanField(required=True)
    profane = BooleanField(required=True)
    user_id = LongField(required=True)

    meta = {
        'indexes': [
            'article_id',
            'user_id'
        ]
    }
