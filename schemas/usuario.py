def usuarioEntity(item) -> dict:
    return {
        "id": item["id"],
        "nombre": item["nombre"],
        "correo": item["correo"]
    }

def usuariosEntity(usuarios) -> list:
    [usuarioEntity(item) for item in usuarios]