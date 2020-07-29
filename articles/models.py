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
    signals,
)

class Group(DynamicDocument):
    """
    This models a 'group' of news to be shown
    """

    tweet_ids = ListField(LongField())
    name = StringField(required=True, max_length=50)
    meta = {
        'indexes': [
        ]
    }

    def __repr__(self):
        return f"""{self.name} group with {len(self.tweet_ids)} tweets
    """