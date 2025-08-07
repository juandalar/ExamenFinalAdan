class BarberoSubject:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, barbero):
        for observador in self.observadores:
            observador.actualizar(barbero)
