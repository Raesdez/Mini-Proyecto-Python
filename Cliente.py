import os
import Datos
import Clases

#Clean screem
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

#Print list
def __printList(lists):
    print("----------------------------------")
    i = 0
    for x in lists:
        i+= 1
        print(i,":",x.nombre,' BsS.',x.precio,' (',x.id,') ')
    print("----------------------------------")

def __searchById(lists,id):
    for product in lists:
        if product.id == id:
            return product
    return None

def init():
    clear()
    print("*************************")
    print("*     Pizzería UCAB     *")
    print("*************************")
    print("Pizza número ", len(pizzaList) + 1)
    print('')
    print('Opciones:')

#Correct answer validation
def validation(y, lists):
    i = 0
    for x in lists:
        i+=1
        if x.id == y:
            return True
            break
    return False


#a partir de aqui. crear el objeto pizza
#lista de pizzas
#total y sub total
#sub total es el total de la pizza a agregar
#total es la suma de todas las pizzas
#Selection of the size of the pizza
def view_size_pizza():
    valid = False
    print('Tamaños disponibles:')
    listSizePizza = Datos.sizesList()
    __printList(listSizePizza)
    while valid == False:
        size = input('Seleccione un tamaño: ')
        valid = validation(size,listSizePizza)
        objectSize = __searchById(listSizePizza,size)
        if valid == False:
            print('Seleccione un tamaño correcto')
    return objectSize

#Selection of Pizza ingredients
def view_ingredients_pizza():
    terminar = False
    valid = False
    ingredientes = []
    print('Ingredientes disponibles:')
    listIngredientsPizza = Datos.ingredientsList()
    __printList(listIngredientsPizza)
    while terminar == False:
        ingredient = input('Seleccione un ingrediente (enter para terminar): ')
        if ingredient == "":
            terminar = True
        else:
            valid = validation(ingredient,listIngredientsPizza)
            objectIngredient = __searchById(listIngredientsPizza,ingredient)
            if valid == False:
                print('Seleccione un ingrediente correcto')
            else:
                ingredientes.append(objectIngredient)
    return ingredientes

#Calculo de total de las pizzas
def calculo_total_pizzas():
    total = 0
    for x in pizzaList:
        total = total + x.calcularTotal()
    return total

#Main
cont = False
opc = False
total = 0
pizzaList = []

while cont == False:
    subtotal = 0
    init()
    pizza = Clases.Pizza()
    pizza.tamano = view_size_pizza()
    init()
    pizza.ingredientes = view_ingredients_pizza()
    print("Usted seleccionó una pizza ",pizza.tamano.nombre," con: ", end = "")
    for x in pizza.ingredientes:
        print(x.nombre, end = " ")
    print("")

    print("Subtotal a pagar por una pizza ",pizza.tamano.nombre,": ", pizza.calcularTotal())
    while opc == False:
        pizzaList.append(pizza)
        fin = input("Desea continuar? [s/n]: ")
        if fin == 'n':
            print("Total a pagar por ",len(pizzaList)," pizzas : ", calculo_total_pizzas())
            print("")
            print('Gracias por su compra')
            cont = True
            break
        elif fin == 's':
            break
        else:
            print('Opción incorrecta')
