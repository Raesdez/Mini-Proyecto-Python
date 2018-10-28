from functools import reduce

class Pizza:

    """ Clase para manejar las pizzas que ordene el cliente  """
    numero = 0
    ingredientes = []
    tamano = ""

    def __init__(self, numero=0,ingredientes=[], tamanos=[]):
        self.numero = nombre
        self.ingredientes = precio
        self.tamanos = tamanos

    """ Calcula el precio total de la pizza sumando las listas que tiene """
    def calcularTotal():
        #suma = reduce((lambda x, y: x + y),map(lambda x: x.precio, ingredientsList()))
        suma = sum(map(lambda i: i.precio,ingredientes))
        for ingrediente in ingredientes:
            suma += ingrediente.precio

        return suma + tamano.precio

class Tamano:

    """ Clase para definir los tamanos de las pizzas """
    id = "00"
    nombre = ""
    precio = 0.00

    def __init__(self,id,nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Ingrediente:

    """ Clase para definir los ingredientes de las pizzas"""

    id = "00"
    nombre = ""
    precio = 0.00

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio
