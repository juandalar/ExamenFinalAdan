class BarberiaDTO:
    def __init__(self, id=None, nombre="", direccion="", telefono=0, ciudad=""):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.ciudad = ciudad 

    def __str__(self):
        return f"BarberiaDTO(id={{self.id}}, nombre='{{self.nombre}}', direccion='{{self.direccion}}', telefono={{self.telefono}}, ciudad={{self.ciudad}})"
