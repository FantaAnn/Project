import wikipedia
import random

wikipedia.set_lang("ru")


def wiki_page(context):
    wiki = wikipedia.page(context)
    if wiki:
        content = wiki.content.split('\n')[0]
        url = wiki.url
        return content, url
    else:
        return "Not Found", "Not Found"


def wiki_image(context):
    wiki = wikipedia.page(context)
    if wiki:
        image = random.choice(wiki.images)
        return image
    else:
        return "Not Found"
