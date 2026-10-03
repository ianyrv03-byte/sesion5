class Envio:
    def __init__(self):
        self._suministros = []

    def agregar_suministro(self, suministro):
        self._suministros.append(suministro)

    def calcular_peso_total(self):
        return sum(s.peso for s in self._suministros)
