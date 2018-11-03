import os
import Datos
import Clases

#If the receipt import fails because FPDF is not imported, the function is
#redefined to return error (9)
try:
    from Recibos import generate_receipt
except:
    def generate_receipt(pizza_list):
        return 9

#Clean screen
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

"""Summary: Imprime la lista de los ingredientes o de las pizzas"""
def __printList(lists):
    print("----------------------------------")
    i = 0
    for x in lists:
        i+= 1
        print(i,":",x.nombre,' BsS.',x.precio,' (',x.id,') ')
    print("----------------------------------")

"""Summary: Devuelve un objeto, buscandolo en una lista por el id"""
def __searchById(lists,id):
    for product in lists:
        if product.id == id:
            return product
    return None

"""Summary: Inicialización de la pizzería"""
def init():
    clear()
    print("*************************")
    print("*     Pizzería UCAB     *")
    print("*************************")
    print("Pizza número ", len(pizzaList) + 1)
    print('')
    print('Opciones:')

"""Summary: Correct answer validation"""
def validation(y, lists):
    i = 0
    for x in lists:
        i+=1
        if x.id == y:
            return True
            break
    return False



"""Summary: Selección del tamaño de la pizza"""
def view_size_pizza():
    valid = False
    print('Tamaños disponibles:')
    listSizePizza = Datos.sizes_list()
    __printList(listSizePizza)
    while valid == False:
        size = input('Seleccione un tamaño: ')
        valid = validation(size,listSizePizza)
        objectSize = __searchById(listSizePizza,size)
        if valid == False:
            print('Seleccione un tamaño correcto')
    return objectSize

"""Summary: Selecciona los ingredientes a agregar en una pizza"""
def view_ingredients_pizza():
    terminar = False
    valid = False
    ingredientes = []
    print('Ingredientes disponibles:')
    listIngredientsPizza = Datos.ingredients_list()
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

"""Summary: Calculo de total de las pizzas"""
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
    if len(pizza.ingredientes) == 0:
        print("Usted seleccionó una pizza ",pizza.tamano.nombre," margarita")
    else:
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
            if(generate_receipt(pizzaList)==9):
                print("El recibo no pudo ser generado")
            print('Gracias por su compra')
            cont = True
            break
        elif fin == 's':
            break
        else:
            print('Opción incorrecta')
