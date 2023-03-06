from fastapi import APIRouter
from config.db import conn
from schemas.usuario import usuarioEntity, usuariosEntity
from models.usuario import Usuario

usuario = APIRouter()


@usuario.get("/usuarios")
def getUsuarios():
    return usuariosEntity(conn.local.usuarios.find())

@usuario.post("/usuarios")
def createUsuarios(user: Usuario):
    nuevo_usuario = dict(user)
    print(nuevo_usuario)
    return "Usuario creado"

@usuario.get("/usuarios/{id}")
def getUsuario():
    return "API usuarios"

@usuario.put("/usuarios/{id}")
def putUsuario():
    return "API usuarios"

@usuario.delete("/usuarios/{id}")
def deleteUsuario():
    return "API usuarios"