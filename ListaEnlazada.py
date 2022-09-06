class Nodo:
    def __init__(self, Valor):
        self.Valor=Valor
        self.SiguienteValor=None
        #self.Posicion=None

        #Devolver el valor en forma de string
    def __str__(self):
        return str(self.Valor)

class ListaEnlazada:
    def __init__(self):
        self.Primero=None
        self.Tamaño=0

        #Agregamos un nodo
    def append(self, Valor):
        NuevoNodo=Nodo(Valor)
        if self.Tamaño==0:
            #NuevoNodo.Posicion=0#nuevo
            self.Primero=NuevoNodo
        else:
            Current=self.Primero
            #Posicion=1#nuevo
            while Current.SiguienteValor!=None:
                Current=Current.SiguienteValor
                #Posicion+=1#nuevo
            #NuevoNodo.Posicion=Posicion
            Current.SiguienteValor=NuevoNodo
        self.Tamaño+=1
        
        #Removemos un nodo
    def Remove(self, Valor):
        if self.Tamaño>0:
            Current=self.Primero
            if Current.Valor==Valor:#Nesecito un if para el que se pueda borrar si se desea el primer nodo
                NodoBorrado=Current
                self.Primero=NodoBorrado.SiguienteValor
                Current=None
                self.Tamaño-=1
            else:
                while Current.SiguienteValor.Valor != Valor:#El while nos va a devolver el nodo anterior al que queremos borrar
                    if Current.SiguienteValor.SiguienteValor==None:#El if es basicamente si el nodo no se encuentra, acaba con el remove
                        return False
                    else:#El else cambia el nodo actual al siguiente para que siga la busqueda
                        Current=Current.SiguienteValor
                NodoBorrado=Current.SiguienteValor#Decimos que encontramos el nodo a borrar  
                if NodoBorrado.SiguienteValor==None:#Si el nodo que vamos a borrar es el ultimo, hacemos que el nodo anterior tenga como siguiente un nodo nulo (None)
                    Current.SiguienteValor=None
                else:#De lo contrario hacemos la union con el nodo que le sigue al nodo borrado
                    Current.SiguienteValor=NodoBorrado.SiguienteValor
                self.Tamaño-=1
        
    def __setitem__(self,indice,NuevoValor):
        if indice>=0 and indice < self.Tamaño:
            Current=self.Primero
            for i in range(indice):
                Current=Current.SiguienteValor
            Current.Valor=NuevoValor
        else:
            raise Exception("indice no valido")

    def __getitem__(self,indice):
        if indice >=0 and indice <self.Tamaño:
            Current=self.Primero
            for i in range(indice):
                Current=Current.SiguienteValor
            return Current.Valor
        else:
            raise Exception("Indice no valido.")

    def __len__(self):
        return self.Tamaño
    
    def __str__(self):
        String="["
        Current=self.Primero
        while Current!=None:
            #String+="("+str(Current.Posicion)+")"
            String+=str(Current)
            if Current.SiguienteValor!=None:
                String+=str(", ")
            Current=Current.SiguienteValor
        String+="]"
        return String