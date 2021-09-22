from cola import Cola

class LineaProduccion:
    def __init__(self, id, componentes, ensamblaje):
        self.id = id
        self.componentes = componentes
        self.tEnsamble = ensamblaje
        self.tiempo = 0
        self.posicion = 1
        self.status = ""
        self.colaPasos = Cola()
        self.pasoActual = None


    def getInfo(self):
        print("ID: ",self.id)
        print("No. componentes: ", self.componentes)
        print("Tiempo de Ensamblaje: ",self.tEnsamble)

    def agregarPaso(self, paso):
        self.colaPasos.agregar(paso)

    def firstStep(self):
        self.pasoActual = self.colaPasos.pop()

    def move(self):
        destino = self.pasoActual['componente']
        if self.posicion == destino:
            self.status = "Listo"
        elif self.posicion > destino:
            self.status = "Moviendo"
            self.posicion -= 1
        elif self.posicion < destino:
            self.status = "Moviendo"
            self.posicion += 1