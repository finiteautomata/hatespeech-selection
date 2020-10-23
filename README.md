# Hatespeech labelling tool



## Instructions

0. Install dependencies

In project directory, run:

```
pipenv shell
pipenv sync
```

1. Get the data

Download `coronavirus-vX.zip` somewhere. Then, do the following

```
unzip hatespeech-articles-dump.zip
cd hatespeech-news
mongoimport coronavirus-argentina-vX.json --db <DATABASE_NAME> --collection article --jsonArray --drop
```

Replace <DATABASE_NAME> with your desired database name. This will load the articles in a collection called `article` (singular name following `mongoengine` convention)


2. Prepare data

```
python bin/merge_articles.py <DATABASE_NAME>
python bin/load_replies.py <DATABASE_NAME>
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

## Selection of news

1. First, select news

Run `notebooks/Sampling with Seeds.ipynb`

2. Dump

```mongoexport -d <DATABASE_NAME> -c article --jsonArray --pretty --query '{"selected":true}' --out dumps/selected-coronavirus-articles.json```
