from bson import ObjectId


def usuarioEntity(item) -> dict:
    return {
        "oid": str(item["_id"]),
        "name": item["name"],
        "reviewerId": item["reviewerId"],
        "reviewerUrl": item["reviewerUrl"],
        "reviewerNumberOfReviews": item["reviewerNumberOfReviews"],
        "isLocalGuide": item["isLocalGuide"],
        "numReviewsEnBD": item["numReviewsEnBD"],
    }

def usuariosEntity(usuarios) -> list:
    return [usuarioEntity(item) for item in usuarios]