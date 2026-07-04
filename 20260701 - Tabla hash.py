class HashTable:

    def __init__(self):
        self.collection = {}

    # método para calular hash
    def hash(self,cadena):
        suma_ascii=0
        for caracter in cadena:
            suma_ascii+=ord(caracter)
        return suma_ascii

    def add(self,clave,valor):
        # calculo el hash de la clave llamando al método .hash
        h=self.hash(clave)

        # chequeo la existencia del hash: si el casillero está vacío, inicializamos un diccionario anidado (diccionario con la clave h dentro del diccionario collection)
        if not h in self.collection:
            self.collection[h]={}

        self.collection[h][clave]=valor
    def remove(self,clave):
        h = self.hash(clave)

        # Verificamos si el hash existe y si la clave real está adentro
        if h in self.collection and clave in self.collection[h]:
            del self.collection[h][clave]

        return
        
    def lookup(self, clave):
        h = self.hash(clave)
        
        if h in self.collection and clave in self.collection[h]:
            return self.collection[h][clave]
        return None