# Hatespeech labelling tool



## Instructions

1. Get the data

Download `hatespeech-articles-dump.zip` somewhere. Then, do the following

```
unzip hatespeech-articles-dump.zip
cd hatespeech-news
mongorestore -d <DATABASE_NAME> articles.bson
```

Replace <DATABASE_NAME> with your desired database name. This will load the articles in a collection called `article` (singular name following `mongoengine` convention)

2. Install dependencies

In project directory, run:

```
pipenv shell
pipenv sync
```

3. Run migrations

```
python manage.py migrate
```

4. Create super user

```
python manage.py createsuperuser
```

5. Start server

```
python manage.py runserver
```
