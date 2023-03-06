from fastapi import FastAPI
from routes.usuario import usuario

app = FastAPI(
    title="API TFF",
    description="Esto es una prueba de API"
)

app.include_router(
    usuario,
)


