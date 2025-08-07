class BarberoDTO:
    def __init__(self, id=None, nombre="", correo="", telefono=0, especialidad=""):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.especialidad = especialidad 

    def __str__(self):
        return f"BarberoDTO(id={{self.id}}, nombre='{{self.nombre}}', correo='{{self.correo}}', telefono={{self.telefono}}, especialidad={{self.especialidad}})"
