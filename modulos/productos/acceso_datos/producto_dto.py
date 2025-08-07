class ProductoDTO:
    def __init__(self, id=None, nombre="", descripcion="", precio=0, categoria=""):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria 

    def __str__(self):
        return f"ProductoDTO(id={{self.id}}, nombre='{{self.nombre}}', descripcion='{{self.descripcion}}', precio={{self.precio}}, categoria={{self.categoria}})"
