class Suministro:
    def __init__(self, nombre, peso):
        if peso <= 0:
            raise ValueError("El peso del suministro debe ser mayor que 0")
        self.nombre = nombre
        self.peso = peso
