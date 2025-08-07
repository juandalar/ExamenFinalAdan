from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from modulos.comentarios.logica.comentario_service import router as comentarios_router
from modulos.productos.logica.productos_service import router as productos_router
from modulos.barberos.logica.barberos_service import router as barberos_router
from modulos.barberias.logica.barberias_service import router as barberias_router

app = FastAPI(title="API Gateway")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(comentarios_router, prefix="/comentarios")
app.include_router(productos_router, prefix="/productos")
app.include_router(barberos_router, prefix="/barberos")
app.include_router(barberias_router, prefix="/barberias")
