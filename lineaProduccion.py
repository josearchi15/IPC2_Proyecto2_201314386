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
        print("ID Linea: ",self.id)
        print("Posicion: ", self.posicion)
        print("Status: ", self.status)
        print("Paso Actual: ", self.pasoActual)

    def agregarPaso(self, paso):
        self.colaPasos.agregar(paso)

    def firstStep(self):
        self.pasoActual = self.colaPasos.pop()
        destino = int(self.pasoActual['componente'])
        if self.posicion == destino:
            self.status = "Lista"
        

    def nextStep(self):
        if self.colaPasos.estaVacia():
            self.status = "Fin"
        else:
            self.pasoActual = self.colaPasos.pop()

    def move(self):
        if self.status == "Fin":
            self.status = "Fin"
        else:
            destino = int(self.pasoActual['componente'])
            if self.posicion > destino:
                self.posicion -= 1
                if self.posicion == destino:
                    self.status = "Lista"
                    # self.nextStep()
                else:
                    self.status = "Moviendo"
            elif self.posicion < destino:
                self.posicion += 1
                if self.posicion == destino:
                    self.status = "Lista"
                    # self.nextStep()
                else:
                    self.status = "Moviendo"
            elif self.posicion == destino:
                self.status = "Lista"
                # self.nextStep()