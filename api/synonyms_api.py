import requests


YANDEX_API = "https://dictionary.yandex.net/api/v1/dicservice.json/lookup"


def find_synonyms(context):
    data = list()
    params = {
            "key": "dict.1.1.20200509T023507Z.2715b218c0e3b5f9.a877d29ee4b0d6ae692a27909160f8a6918218d4",
            "text": context,
            "lang": "ru-ru"
        }
    try:
        response = requests.get(YANDEX_API, params=params).json()['def'][0]['tr']
        for i in response:
            for j in i['syn']:
                data.append(j['text'])
    except:
        data.append("Синонимы не найдены")
    return data
