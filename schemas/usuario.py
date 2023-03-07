def usuarioEntity(item) -> dict:
    return {
        "name": item["name"],
        "reviewerId": item["reviewerId"],
        "reviewerUrl": item["reviewerUrl"],
        "reviewerNumberOfReviews": item["reviewerNumberOfReviews"],
        "isLocalGuide": item["isLocalGuide"],
        "numReviewsEnBD": item["numReviewsEnBD"],
    }

def usuariosEntity(usuarios) -> list:
    [usuarioEntity(item) for item in usuarios]