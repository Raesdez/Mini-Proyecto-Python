#---------------- Ramón Sosa ------------------
import Datos
import os

def viewProducts():
    while True:
        answer = input("Indique el tipo de producto que desea consultar (i: ingrediente, t: tamano): ")
        print("")
        if(answer == "I" or answer == "i"):
            lists = Datos.ingredientsList()
            print("Mostrando todos los ingredientes: ")
        elif(answer == "T" or answer == "t"):
            lists = Datos.sizesList()
            print("Mostrando todos los tamanos de pizza: ")
        else:
            print("Seleccione una opcion valida")
            continue

        __printList(lists)
        print("")
        input("Presione cualquier tecla para volver")
        break

def addProduct():
    while True:
        answer = input("Indique el tipo de producto que desea agregar (i: ingrediente, t: tamano): ")

        #Constructing the object
        nombre = str(input('Indique el nombre del producto: '))
        id = str(input('Indique el codigo del producto: '))
        precio = float(input('Indique el precio del producto: '))

        if(answer == "I" or answer == "i"):
            if(Datos.saveIngredient(Datos.Ingrediente(id,nombre,precio))==1):
                print("Ya existe un ingrediente con este identificador, por favor intente nuevamente")
                continue
            print()

        elif(answer == "T" or answer == "t"):
            if(Datos.saveSize(Datos.Tamano(id,nombre,precio))):
                print("Ya existe un tamano con este identificador, por favor intente nuevamente")
                continue
            print()
        else:
            print("Seleccione una opcion valida")
            continue

        print("")
        input("Producto agregado, presione cualquier tecla para continuar")
        break

def deleteProduct():
    while True:
        answer = input("Indique el tipo de producto que desea eliminar (i: ingrediente, t: tamano): ")
        print("")
        if(answer == "I" or answer == "i"):
            lists = Datos.ingredientsList()
            func = Datos.deleteIngredient
            print("Mostrando todos los ingredientes: ")
        elif(answer == "T" or answer == "t"):
            lists = Datos.sizesList()
            func = Datos.deleteSize
            print("Mostrando todos los tamanos de pizza: ")
        else:
            print("Seleccione una opcion valida")
            continue

        __printList(lists)
        print("")

        id = input("Indique el Id del producto a eliminar: ")
        product = __searchById(lists,id)
        if(product != None):
            func(product)
        else:
            print("Seleccione una opcion valida")
            continue

        input("Producto eliminado, presione cualquier tecla para continuar: ")
        break

def exit():
    while True:
        answer = input("Seguro que desea salir? [s/n]: ")

        if (answer == 's' or answer == 'S'):
            print("Hasta luego")
            quit()
        elif (answer == 'n' or answer == 'N'):
            break
        else:
            print("Seleccione una opcion valida")

#-------------------------  Private  ---------------------------------
def __printList(lists):
    print("----------------------------------")
    i = 0
    for x in lists:
        i+= 1
        print(i,":",x.id,',',x.nombre,',',x.precio)
    print("----------------------------------")

def __searchById(lists,id):
    for product in lists:
        if product.id == id:
            return product
    return None
#-------------------------  Main  ---------------------------------
switcher = {
        1: viewProducts,
        2: addProduct,
        3: deleteProduct,
        0: exit,
    }

while True:

    os.system('clear')
    print("------------------------------------------")
    print("Bienvenido al Administrador de la Pizzeria")
    print("------------------------------------------")
    print("")

    #Menú
    print("Seleccione alguna de las siguientes opciones:")
    print("1: Ver productos")
    print("2: Agregar un producto")
    print("3: Eliminar un producto")
    print("0: Salir")

    #try:
    func = switcher.get(int(input("Opcion: ")), lambda: "Seleccione una opcion valida")
    os.system('clear')
    func()
    #except:
        #print("Error desconocido")
