import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/barberos/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, barbero):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, barbero):
        mensaje = f"[Usuario] Se envió alerta al usuario {barbero.especialidad} por su negativo."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, barbero):
        mensaje = f"[Admin] Atención: negativo registrado de {barbero.especialidad}: '{barbero.nombre}'"
        print(mensaje)
        logging.info(mensaje)
