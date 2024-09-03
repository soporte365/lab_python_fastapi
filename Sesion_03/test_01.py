
class Carro():
    ruedas = 4

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        veloc = self.velocidad - self.aceleracion
        if veloc < 0:
            veloc =0
        self.velocidad = veloc

car1 = Carro("Negro", 50)
car1.acelerar()
print("La acelleración del carro {} es {}".format(car1.color, car1.velocidad))


