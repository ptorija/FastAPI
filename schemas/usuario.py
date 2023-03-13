from bson import ObjectId

def usuarioAlgoritmoEntity(item, idArtifical) -> dict:
    return{
        "oid": str(item["_id"]),
        "idArtificial": idArtifical
    }

def usuariosAlgoritmoEntity(usuarios) -> list:
    result = list()
    idArtificial = 1
    for usuario in usuarios:
        result.append(usuarioAlgoritmoEntity(usuario, idArtificial))
        idArtificial = idArtificial + 1
    return result

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