from datetime import datetime

class ClienteDTO:
    def __init__(self, id=None, nombre="", email="", telefono="", password_hash="", activo=True, fecha_registro=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.password_hash = password_hash
        self.activo = activo
        self.fecha_registro = fecha_registro or datetime.now()

    def __str__(self):
        return f"ClienteDTO(id={self.id}, nombre='{self.nombre}', email='{self.email}', telefono='{self.telefono}', activo={self.activo})"
