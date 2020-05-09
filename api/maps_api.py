import requests


def find_delta(json_response):
    toponym_delta = json_response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]["boundedBy"]["Envelope"]

    delta_1 = str(round(abs(float(toponym_delta["lowerCorner"].split()[0]) -
                            float(toponym_delta["upperCorner"].split()[0])), 3))
    delta_2 = str(round(abs(float(toponym_delta["lowerCorner"].split()[1]) -
                            float(toponym_delta["upperCorner"].split()[1])), 3))
    return ",".join([delta_1, delta_2])


def find_object_info(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(
        geocoder_api_server, params=geocoder_params)
    return response


def take_map_picture(coordinates, delta, map_type, point_type):
    coordinates = ','.join(coordinates.split(' '))
    point_data = ','.join((coordinates, point_type))

    map_api_server = "http://static-maps.yandex.ru/1.x/"

    map_params = {
                "ll": coordinates,
                "spn": delta,
                "l": map_type,
                "pt": point_data
            }

    response = requests.get(map_api_server, params=map_params)
    return response


def find_object_coordinates(json_response):
    coordinates = json_response["response"]["GeoObjectCollection"][
                "featureMember"][0]["GeoObject"]["Point"]["pos"]
    return coordinates