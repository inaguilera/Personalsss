from math import pi
class Circulo:
    def __init__(self,r):
        self.radio=r

    def obtener_area(self):
        area = (self.radio**2)*pi
        return area

    def obtener_perimetro(self):
        perimetro = 2*pi*self.radio
        return perimetro

    def __str__(self):
        return 'Es un circulo de area {} y perimetro {}'.format(Circulo.obtener_area(self),Circulo.obtener_perimetro(self))

cir = Circulo(3)
print(cir)