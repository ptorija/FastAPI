from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import conn
from schemas.review import reviewEntity, reviewsEntity
from models.review import ReviewMongo

review = APIRouter(
    tags=["Reviews"]
)
db = conn["tfg"]
coll = db["reviews"]


@review.get("/reviews")
def get_Reviews():
    result = coll.find({})
    return reviewsEntity(result)


@review.get("/reviews/{id}")
def get_Reviews(id):
    rewiew_bd =reviewEntity(coll.find_one({"_id":ObjectId(id)}))
    return dict(rewiew_bd)


@review.post("/revievs")
def create_Review(review: ReviewMongo):
    coll.insert_one(review.dict())
    return "Review creada"


