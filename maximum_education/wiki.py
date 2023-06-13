import wikipedia

def get_wiki_article(artikle):
    wikipedia.set_lang("ru")

    try:
        return f'{wikipedia.summary(title=artikle, sentences=5)}'
    except wikipedia.WikipediaException:
        return "не удалось найти информацию"