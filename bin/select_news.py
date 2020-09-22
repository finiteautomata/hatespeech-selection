"""
Mark news as selected=True
"""

import fire
from hatespeech_models import Article
from mongoengine import connect

def select_articles(database, unselect_all_first=True):
    """
    Mark articles as selected
    """
    connect(database)

    if unselect_all_first:
        Article.objects.update(selected=False)

    seeds = [
        "China", "chino", "Cuba", "cubano", "bolivia",
        "Trump", "judío", "camionero", "agresor",
        "policía", "ladrón", "reprimir", "represión",
        "juez", "justicia", "penal", "criminal",
        "delito", "mamá", "género",
        "aborto", "actriz", "feminista", "madre", "enfermera", "médica",
        "piqueteros", "villa", "monos",
        "Agustina", "Pichot",
        "femicidios", "mujer", "trans",
        "cristina", "macri", "morales", "canosa", "evo",
        "\"movimientos sociales\"",
        "protesta",
        "\"organizaciones sociales\"",
        "\"villa\"",
        "\"Nati Jota\"",
        "\"Viale\"",
        "\"Ernestina Pais\"",
        "\"Mica Viciconte\"",
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

    queries = {}

    for word in seeds:
        query = Article.objects(dummy__ne=True, comments__19__exists=True).search_text(word)
        nuevos = 0
        queries[word] = query

        for art in query:
            if art.id not in seed_ids:
                nuevos += 1
                seed_ids.add(art.id)
                seed_articles.append(art)
        print(f"{word} ---> {len(seed_articles)}, {nuevos} nuevos")

    print("Tenemos {len(seed_ids)}")
    updated = Article.objects(id__in=seed_ids).update(set__selected=True)
    print(f"Marcados como seleccionados {updated} artículo")

if __name__ == '__main__':
    fire.Fire(select_articles)
