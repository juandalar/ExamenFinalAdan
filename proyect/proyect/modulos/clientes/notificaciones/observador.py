import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/clientes/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, cliente):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, cliente):
        mensaje = f"[Usuario] Email de bienvenida enviado al cliente {cliente.email} - {cliente.nombre}"
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, cliente):
        mensaje = f"[Admin] Nuevo cliente registrado: {cliente.nombre} ({cliente.email}) - Tel: {cliente.telefono}"
        print(mensaje)
        logging.info(mensaje)