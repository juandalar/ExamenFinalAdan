class ProductoSubject:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, producto):
        for observador in self.observadores:
            observador.actualizar(producto)
