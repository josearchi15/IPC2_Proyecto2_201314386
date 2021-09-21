
class LineaProduccion:
    def __init__(self, id, componentes, ensamblaje):
        self.id = id
        self.componentes = componentes
        self.tEnsamble = ensamblaje
        self.tiempo = 0
        self.posicion = 0

    def getInfo(self):
        print("ID: ",self.id)
        print("No. componentes: ", self.componentes)
        print("Tiempo de Ensamblaje: ",self.tEnsamble)