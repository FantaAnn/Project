import requests


YANDEX_API = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


def translate_word(word, language):
    params = {
            "key": 'trnsl.1.1.20200402T021916Z.a0baf50961a7f3a2.c86f1003e62bc2e66c5abaadd3460cc06a1edceb',
            "text": word,
            "lang": language
        }
    try:
        content = requests.get(YANDEX_API, params=params).json()['text']
        return content[0]
    except:
        return "Перевести не удалось"


def get_languages():
    params = {
        "key": "trnsl.1.1.20200402T021916Z.a0baf50961a7f3a2.c86f1003e62bc2e66c5abaadd3460cc06a1edceb"
    }
    content = requests.get("https://translate.yandex.net/api/v1.5/tr.json/getLangs?ui=en", params=params).json()['dirs']
    return content