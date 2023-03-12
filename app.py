from fastapi import FastAPI
from routes.usuario import usuario
from routes.restaurante import restaurante

app = FastAPI(
    title="API TFF",
    description="Esto es una prueba de API"
)

app.include_router(
    restaurante,
)
app.include_router(
    usuario
)



