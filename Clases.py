class Pizza:
    """ Clase para manejar las pizzas que ordene el cliente  """

    """ Clase para manejar las pizzas que ordene el cliente  """

    def __init__(self, numero=0,ingredientes=None, tamano=""):
        self.numero = numero
        if ingredientes is None:
            ingredientes = []
            self.ingredientes = ingredientes
        self.tamano = tamano

    """ Calcula el precio total de la pizza sumando las listas que tiene """
    def calcularTotal(self):
        suma = sum(map(lambda i: i.precio,self.ingredientes))
        return suma + self.tamano.precio

class Tamano:

    """ Clase para definir los tamanos de las pizzas """
    def __init__(self,id="00",nombre="", precio=0.00):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Ingrediente:

    """ Clase para definir los ingredientes de las pizzas"""
    def __init__(self, id="00", nombre="", precio=0.00):
        self.id = id
        self.nombre = nombre
        self.precio = precio
