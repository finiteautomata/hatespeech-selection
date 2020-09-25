"""
Mark news as selected=True
"""

import fire
from hatespeech_models import Article, Reply
from mongoengine import connect

def select_articles(database, unselect_all_first=True):
    """
    Mark articles as selected
    """
    connect(database)

    if unselect_all_first:
        Article.objects.update(selected=False)

    seeds = [
        "China",
        "Cuba",
        "cubano",
        "bolivia",
        "Trump",
        "judío",
        "camionero",
        "agresor",
        #"policía",
        "\"presos\"",
        "ladrón",
        "reprimir",
        "represión",
        #"juez",
        #"justicia",
        "penal",
        "criminal",
        "delito", "mamá",
        "\"de género\"",
        "\"aborto\"",
        "\"actriz\"",
        "feminista",
        "piqueteros",
        "villa",
        "monos",
        "\"Pichot\"",
        "femicidio",
        #"cristina",
        #"macri",
        "\"Evo Morales\"",
        "\"canosa\"",
        "\"movimientos sociales\"",
        "\"protesta\"",
        "\"médica\"",
        "\"Florencia Kirchner\"",
        "\"enfermera\"",
        "\"madre\"",
        "\"organizaciones sociales\"",
        "\"villa\"",
        "\"Nati Jota\"",
        "\"Ernestina Pais\"",
        "\"Mica Viciconte\"",
        "\"Funes Ugarte\"",
        "\"la modelo\"",
        "\"la actriz\"",
        "\"la periodista\"",
        "\"Carla\"",
        "\"la conductora\"",
        "\"la cantante\"",
        "\"Cande\"",
        "\"personal doméstico\"",
        "\"empleadas\"",
    ]


    seed_ids = set()
    seed_articles = []
    print("Agregando por búsqueda en artículo")


    for word in seeds:
        query = Article.objects(dummy__ne=True, comments__19__exists=True).search_text(word)
        nuevos = 0

        for art in query:
            if art.id not in seed_ids:
                nuevos += 1
                seed_ids.add(art.id)
                seed_articles.append(art)
        print(f"{word:<30} ---> {len(seed_articles):<5}, {nuevos:<4} nuevos")

    print("Seleccionando por comentarios")

    comment_seeds = [
        "judío",
        "sionista",
        "\"terrorista\"",
        "monos",
        "\"soros\"",
        "\"puto\"",
        "travesti",
        "\"trolo\"",
        "maricon",
        "\"degenerado\"",
        "\"trabuco\"",
        "picaporte",
    ]

    for word in comment_seeds:
        nuevos = 0

        for rep in Reply.objects.search_text(word):
            if len(rep.article.comments) < 20:
                continue

            art = rep.article

            if art.id not in seed_ids:
                nuevos += 1
                seed_ids.add(art.id)
                seed_articles.append(art)

        print(f"{word:<30} ---> {len(seed_articles):<5}, {nuevos:<4} nuevos")


    print(f"Tenemos {len(seed_ids)}")

    distinct_titles = set(art.title for art in seed_articles)

    print(f"Tenemos {len(distinct_titles)} títulos distintos")
    updated = Article.objects(id__in=seed_ids).update(set__selected=True)
    print(f"Marcados como seleccionados {updated} artículos")

if __name__ == '__main__':
    fire.Fire(select_articles)
