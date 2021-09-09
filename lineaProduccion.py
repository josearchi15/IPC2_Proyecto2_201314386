
class LineaProduccion:
    def __init__(self, id, componentes, ensamblaje):
        self.id = id
        self.componentes = componentes
        self.tEnesamble = ensamblaje
        self.tiempo = 0
        self.posicion = 0

    def mover(self, componente):
        if self.posicion > componente:
            dif = self.posicion-componente
        elif componente > self.posicion:
            dif = componente-self.posicion
        
        self.tiempo += dif