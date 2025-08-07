import json
import hashlib
from fastapi import APIRouter, Request, HTTPException
from modulos.clientes.acceso_datos.get_factory import obtener_fabrica
from modulos.clientes.acceso_datos.clientes_dto import ClienteDTO
from modulos.clientes.notificaciones.sujeto import ClienteSubject
from modulos.clientes.notificaciones.observador import UsuarioNotificador, AdminNotificador

# Funciones de hash simples
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

dao = obtener_fabrica().crear_dao()
sujeto = ClienteSubject()
sujeto.agregar_observador(UsuarioNotificador())
sujeto.agregar_observador(AdminNotificador())
router = APIRouter()

@router.post("/")
async def crear_cliente(req: Request):
    data = await req.json()
    cliente = ClienteDTO(
        nombre=data["nombre"],
        email=data["email"],
        telefono=data.get("telefono", ""),
        password_hash=hash_password(data["password"])
    )
    dao.guardar(cliente)
    sujeto.notificar(cliente)
    return {"mensaje": "Cliente registrado correctamente."}

@router.get("/")
def obtener_clientes():
    return [c.__dict__ for c in dao.obtener_todos()]

@router.get("/{id}")
def obtener_cliente(id: int):
    cliente = dao.obtener_por_id(id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente.__dict__

@router.put("/{id}")
async def actualizar_cliente(id: int, req: Request):
    data = await req.json()
    actualizado = ClienteDTO(
        id=id,
        nombre=data["nombre"],
        email=data["email"],
        telefono=data["telefono"],
        password_hash=hash_password(data["password"])
    )
    dao.actualizar(actualizado)
    return {"mensaje": "Cliente actualizado"}

@router.delete("/{id}")
def eliminar_cliente(id: int):
    dao.eliminar(id)
    return {"mensaje": "Cliente eliminado"}