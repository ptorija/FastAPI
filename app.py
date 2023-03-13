import uvicorn
from fastapi import FastAPI
from routes.usuario import usuario
from routes.restaurante import restaurante
from routes.reviews import review

app = FastAPI(
    title="API TFF",
    description="Esto es una prueba de API",
)

app.include_router(
    restaurante
)
app.include_router(
    usuario
)
app.include_router(
    review
)

if __name__ == '__main__':
    uvicorn.run('app:app', host='0.0.0.0', port=8000)

