import json
from fastapi import APIRouter, Request, HTTPException
from modulos.barberos.acceso_datos.get_factory import obtener_fabrica
from modulos.barberos.acceso_datos.barbero_dto import BarberoDTO
from modulos.barberos.notificaciones.sujeto import BarberoSubject
from modulos.barberos.notificaciones.observador import UsuarioNotificador, AdminNotificador
dao = obtener_fabrica().crear_dao()
sujeto = BarberoSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())
router = APIRouter()

@router.post("/")
async def crear_barbero(req: Request):
    data = await req.json()
    barbero = BarberoDTO(
        nombre=data["nombre"],correo=data["correo"],telefono=int(data["telefono"]),especialidad=data["especialidad"] )
    dao.guardar(barbero)
    return {"mensaje": "Barbero almacenado correctamente."}
@router.get("/")
def obtener_barberos():
    return [c.__dict__ for c in dao.obtener_todos()]
@router.get("/{id}")
def obtener_barbero(id: int):
    barbero = dao.obtener_por_id(id)
    if not barbero:
        raise HTTPException(status_code=404, detail="Barbero no encontrado")
    return barbero.__dict__
@router.put("/{id}")
async def actualizar_barbero(id: int, req: Request):
    data = await req.json()
    actualizado = BarberoDTO(
        id=id,
        nombre=data["nombre"],
        correo=data["correo"],
        telefono=int(data["telefono"]),
        especialidad=data["especialidad"]
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Barbero actualizado"}
@router.delete("/{id}")
def eliminar_barbero(id: int):
    dao.eliminar(id)
    return {"mensaje": "Barbero eliminado"}
