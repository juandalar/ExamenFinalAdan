import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/productos/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, producto):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, producto):
        mensaje = f"[Usuario] Se envió alerta al usuario {producto.categoria} por su producto negativo."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, producto):
        mensaje = f"[Admin] Atención: producto negativo registrado de {producto.categoria}: '{producto.nombre}'"
        print(mensaje)
        logging.info(mensaje)
