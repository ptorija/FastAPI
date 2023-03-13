from bson import ObjectId
from fastapi import APIRouter
from config.db import conn
from schemas.restaurante import restauranteEntity, restaurantesEntity
from models.restaurante import RestauranteMongo


restaurante = APIRouter(
    tags=["Restaurantes"]
)
db = conn["tfg"]
coll = db["restaurants"]


@restaurante.get("/restaurantes")
def get_Restaurantes():
    result = coll.find({})
    return restaurantesEntity(result)


@restaurante.get("/restaurantes/{id}")
def get_Restaurante(id):
    usuario_id = restauranteEntity(coll.find_one({"_id": ObjectId(id)}))
    return dict(usuario_id)

@restaurante.post("/restaurantes")
def create_Restaurante(restaurant: RestauranteMongo):
    coll.insert_one(restaurant.dict())
    return "Restaurante creado"
