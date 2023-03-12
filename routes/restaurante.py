from bson import ObjectId

from schemas.restaurante import restauranteEntity
from schemas.restaurante import restaurantesEntity
from models.restaurante import RestauranteMongo
from fastapi import APIRouter
from config.db import conn

restaurante = APIRouter()
db = conn["tfg"]
coll = db["restaurants"]


@restaurante.get("/restaurantes")
def getRestaurantes():
    result = coll.find({})
    return restaurantesEntity(result)


@restaurante.get("/restaurantes/{id}")
def getUsuario(id):
    usuario_id = restauranteEntity(coll.find_one({"_id": ObjectId(id)}))
    return dict(usuario_id)

@restaurante.post("/restaurantes")
def createUsuarios(restaurant: RestauranteMongo):
    nuevo_restaurante = dict(restaurant)
    coll.insert_one(nuevo_restaurante)
    print(nuevo_restaurante)
    return "Restaurante creado"
