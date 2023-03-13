def restauranteEntity(item) -> dict:
    if ("price_level" in item):
        price_level = item["price_level"]
    else:
        price_level = None
    return {
        "oid": str(item["_id"]),
        "formatted_address": item["formatted_address"],
        "lat": item["geometry"]["location"]["lng"],
        "lng": item["geometry"]["location"]["lat"],
        "name": item["name"],
        "photo_url": item["photo_url"],
        "place_id": item["place_id"],
        "price_level": price_level,
        "rating": item["rating"],
        "types": item["types"],
        "user_ratings_total": item["user_ratings_total"]
    }


def restaurantesEntity(restaurantes) -> dict:
    return [restauranteEntity(item) for item in restaurantes]


def restauranteAlgoritmoEntity(item, idArtificial) -> dict:
    return {
        "oid": str(item["_id"]),
        "id": idArtificial
    }


def restaurantesAlgoritmoEntity(restaurantes) -> list:
    idArtificial = 1
    result = list()
    for restaurante in restaurantes:
        result.append(restauranteAlgoritmoEntity(restaurante,idArtificial))
        idArtificial = idArtificial + 1
    return restaurante
