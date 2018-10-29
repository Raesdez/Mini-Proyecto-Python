import os
import Datos

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
    print("Pizza número ", numeroPizza)
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
def view_ingredientsp_izza():
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



#Main
cont = False
opc = False
numeroPizza = 1
total = 0
while cont == False:
    subtotal = 0
    init()
    objectSize = view_size_pizza()
    init()
    ingredientes = view_ingredientsp_izza()
    print("Usted seleccionó una pizza ",objectSize.nombre," con: ", end = "")
    for x in ingredientes:
        print(x.nombre, end = " ")
    print("")
    print("Subtotal a pagar por una pizza ",objectSize.nombre,": ")
    while opc == False:
        fin = input("Desea continuar? [s/n]: ")
        if fin == 'n':
            print('Gracias por su compra')
            cont = True
            break
        elif fin == 's':
            numeroPizza += 1
            break
        else:
            print('Opción incorrecta')
