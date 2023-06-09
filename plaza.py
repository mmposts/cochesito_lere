from coche import Coche
class Plaza:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.coche = None

    def aparcar(self, coche: Coche):
        if self.esta_disponible():
            raise Exception("Ya hay un coche aparcado")

        self.coche = coche

    def desocupar(self):
        self.coche = None

    def esta_disponible(self):
        if self.coche:
            return False
        
        return True

    def __str__(self):
        return "VACIO" if self.esta_disponible() else str(self.coche)

