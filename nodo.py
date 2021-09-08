class Nodo:
    def __init__(self,datoInicial):  #constructor recibe dato/info del nodo
        self.dato = datoInicial      #asigna dato
        self.siguiente = None        #asigna null al apuntador siguiente del dato

    def obtenerDato(self):           #retorna el dato/info del nodo, puede ser un valor primitivo como un objeto
        return self.dato

    def obtenerSiguiente(self):      #nos brinda el dato siguiente, este puede tener un valor com dato y con siguiente eventualmente
        return self.siguiente

    def asignarDato(self,nuevodato): #aqui solo estamos asignando un dato/info a nuestro nodo, puede ser valor primitivo u objeto
        self.dato = nuevodato

    def asignarSiguiente(self,nuevosiguiente):  #asigna un valor a siguiente, esto quiere decir que ahora siguiente ya no es null
        self.siguiente = nuevosiguiente