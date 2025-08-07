import json
from fastapi import APIRouter, Request, HTTPException
from modulos.barberias.acceso_datos.get_factory import obtener_fabrica
from modulos.barberias.acceso_datos.barberia_dto import BarberiaDTO
from modulos.barberias.notificaciones.sujeto import BarberiaSubject
from modulos.barberias.notificaciones.observador import UsuarioNotificador, AdminNotificador
dao = obtener_fabrica().crear_dao()
sujeto = BarberiaSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())
router = APIRouter()

@router.post("/")
async def crear_barberia(req: Request):
    data = await req.json()
    barberia = BarberiaDTO(
        nombre=data["nombre"],direccion=data["direccion"],telefono=int(data["telefono"]),ciudad=data["ciudad"] )
    dao.guardar(barberia)
    return {"mensaje": "Barberia almacenada correctamente."}
@router.get("/")
def obtener_barberia():
    return [c.__dict__ for c in dao.obtener_todos()]
@router.get("/{id}")
def obtener_barberia(id: int):
    barberia = dao.obtener_por_id(id)
    if not barberia:
        raise HTTPException(status_code=404, detail="Barberia no encontrada")
    return barberia.__dict__
@router.put("/{id}")
async def actualizar_barberia(id: int, req: Request):
    data = await req.json()
    actualizado = BarberiaDTO(
        id=id,
        nombre=data["nombre"],
        direccion=data["direccion"],
        telefono=int(data["telefono"]),
        ciudad=data["ciudad"]
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Barberia actualizado"}
@router.delete("/{id}")
def eliminar_barberia(id: int):
    dao.eliminar(id)
    return {"mensaje": "Barberia eliminado"}
