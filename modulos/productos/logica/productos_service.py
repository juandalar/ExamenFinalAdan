import json
from fastapi import APIRouter, Request, HTTPException
from modulos.productos.acceso_datos.get_factory import obtener_fabrica
from modulos.productos.acceso_datos.producto_dto import ProductoDTO
from modulos.productos.notificaciones.sujeto import ProductoSubject
from modulos.productos.notificaciones.observador import UsuarioNotificador, AdminNotificador
dao = obtener_fabrica().crear_dao()
sujeto = ProductoSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())
router = APIRouter()

@router.post("/")
async def crear_producto(req: Request):
    data = await req.json()
    producto = ProductoDTO(
        nombre=data["nombre"],descripcion=data["descripcion"],precio=int(data["precio"]),categoria=data["categoria"] )
    dao.guardar(producto)
    return {"mensaje": "Producto almacenado correctamente."}
@router.get("/")
def obtener_productos():
    return [c.__dict__ for c in dao.obtener_todos()]
@router.get("/{id}")
def obtener_producto(id: int):
    producto = dao.obtener_por_id(id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto.__dict__
@router.put("/{id}")
async def actualizar_producto(id: int, req: Request):
    data = await req.json()
    actualizado = ProductoDTO(
        id=id,
        nombre=data["nombre"],
        descripcion=data["descripcion"],
        precio=int(data["precio"]),
        categoria=data["categoria"]
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Producto actualizado"}
@router.delete("/{id}")
def eliminar_producto(id: int):
    dao.eliminar(id)
    return {"mensaje": "Producto eliminado"}
