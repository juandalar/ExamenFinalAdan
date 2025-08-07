import logging
from abc import ABC, abstractmethod

# Configurar logging para guardar notificaciones en archivo
logging.basicConfig(
    filename="modulos/barberias/logs/notificaciones.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Observador(ABC):
    @abstractmethod
    def actualizar(self, barberia):
        pass

class UsuarioNotificador(Observador):
    def actualizar(self, barberia):
        mensaje = f"[Usuario] Se envió alerta al usuario {barberia.ciudad} por su barberia negativa."
        print(mensaje)
        logging.info(mensaje)

class AdminNotificador(Observador):
    def actualizar(self, barberia):
        mensaje = f"[Admin] Atención: barberia negativa registrado de {barberia.ciudad}: '{barberia.nombre}'"
        print(mensaje)
        logging.info(mensaje)
