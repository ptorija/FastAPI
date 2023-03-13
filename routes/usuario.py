from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import conn
from schemas.usuario import usuarioEntity, usuariosEntity, usuariosAlgoritmoEntity
from models.usuario import UsuarioMongo

usuario = APIRouter(
    tags=["Usuarios"]
)
db = conn["tfg"]
coll = db["users"]


@usuario.get("/usuarios")
def get_Usuarios():
    result = coll.find({})
    return usuariosEntity(result)


@usuario.get("/usuarios/{id}")
def get_Usuario(id):
    usuario_bd = usuarioEntity(coll.find_one({"_id":ObjectId(id)}))
    return dict(usuario_bd)


@usuario.post("/usuarios")
def create_Usuarios(user: UsuarioMongo):
    nuevo_usuario = dict(user)
    coll.insert_one(nuevo_usuario)
    print(nuevo_usuario)
    return "Usuario creado"


@usuario.put("/usuarios/{id}")
def put_Usuario(id: str, user: UsuarioMongo):
    return coll.find_one_and_update(
        {"_id": ObjectId(id)},
        {{"$set": dict(user)}}
    )


@usuario.delete("/usuarios/{id}")
def delete_Usuario(id):
    myquery = {"_id":ObjectId(id)}
    coll.delete_one(myquery)
    return "Usuario Borrado con éxito"

@usuario.get("/usuarios/usersWithReviews/{count}")
def get_Users_With_X_Reviews(count):
    myquery = {"numReviewsEnBD": {"$gte": int(count)}}
    usuarios = coll.find(myquery)
    return usuariosEntity(usuarios)


@usuario.get("/usuarios/")
def get_Users_With_X_Reviews_Algorythm(count):
    usuarios = coll.find({"numReviewsEnBD":{"$gte":int(count)}},{"_id":1})

    return usuariosAlgoritmoEntity(usuarios)

