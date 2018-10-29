import os
import Datos

#Limpia la pantalla
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

#Imprime la lista
def __printList(lists):
    print("----------------------------------")
    i = 0
    for x in lists:
        i+= 1
        print(i,":",x.nombre,' BsS.',x.precio,' (',x.id,') ')
    print("----------------------------------")

def init():
    clear()
    print("*************************")
    print("*     Pizzería UCAB     *")
    print("*************************")
    print("Pizza número ", numeroPizza)
    print('')
    print('Opciones:')

#Validacion de respuesta correcta
def validation(y, lists):
    i = 0
    for x in lists:
        i+=1
        if x.id == y:
            return True
            break
    return False

#Seleccion del tamano de la pizza
def viewSizePizza():
    valid = False
    print('Tamaños disponibles:')
    listSizePizza = Datos.sizesList()
    __printList(listSizePizza)
    while valid == False:
        size = input('Seleccione un tamaño: ')
        valid = validation(size,listSizePizza)
        if valid == False:
            print('Seleccione un tamaño correcto')

#Seleccion de los ingredientes de la Pizza
def viewIngredientsPizza():
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
            if valid == False:
                print('Seleccione un ingrediente correcto')
            else:
                ingredientes.append(ingredient)





#Main
cont = False
opc = False
numeroPizza = 1
ingredientes = []
while cont == False:
    init()
    viewSizePizza()
    init()
    viewIngredientsPizza()
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
