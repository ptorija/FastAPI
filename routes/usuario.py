from bson.objectid import ObjectId
from fastapi import APIRouter
from config.db import conn
from schemas.usuario import usuarioEntity, usuariosEntity
from models.usuario import UsuarioMongo

usuario = APIRouter()
db = conn["tfg"]
coll = db["users"]


@usuario.get("/usuarios")
def getUsuarios():
    result = coll.find({})
    return usuariosEntity(result)


@usuario.post("/usuarios")
def createUsuarios(user: UsuarioMongo):
    nuevo_usuario = dict(user)
    coll.insert_one(nuevo_usuario)
    print(nuevo_usuario)
    return "Usuario creado"


@usuario.get("/usuarios/{id}")
def getUsuario(id):
    usuario_id = usuarioEntity(coll.find_one({"_id":ObjectId(id)}))
    return dict(usuario_id)


@usuario.put("/usuarios/{id}")
def putUsuario():
    return "API usuarios"


@usuario.delete("/usuarios/{id}")
def deleteUsuario(id):
    myquery = {"_id":ObjectId(id)}
    coll.delete_one(myquery)
    return "Usuario Borrado con éxito"

@usuario.get("/usuarios/usersWithReviews/{count}")
def getUsersWithReviews(count):
    myquery = {"numReviewsEnBD": {"$gte": int(count)}}
    x = coll.find(myquery)
    return usuariosEntity(x)
