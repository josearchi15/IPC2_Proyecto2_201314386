from cola import Cola

class Producto:
    def __init__(self, nombre, instrucciones):
        self.nombre = nombre
        self.instrucciones = instrucciones
        self.pasos = Cola()
        self.tiempo = 0

    def getPasos(self):
        arr = self.instrucciones.split('p')
        puntoLinea = Cola()
        puntoComponente = Cola()
        
        for i in range(len(arr)-1):
            if i%2 == 0:
                # print(arr[i]," es par")
                puntoLinea.agregar(arr[i])
            else:
                # print(arr[i]," es impar")
                puntoComponente.agregar(arr[i])

        while not puntoLinea.estaVacia() and not puntoComponente.estaVacia():
            punto = {
                "linea": puntoLinea.pop().split("L")[1],
                "componente": puntoComponente.pop().split("C")[1]
            }
            self.pasos.agregar(punto)

# p1 = Producto("Smartwatch", "L1pC2pL2pC1pL2pC2pL1pC4p")
# p1.getPasos()