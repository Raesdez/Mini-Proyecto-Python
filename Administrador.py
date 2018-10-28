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
            print("----------------------------------")
        elif(answer == "T" or answer == "t"):
            lists = Datos.sizesList()
            print("Mostrando todos los tamanos de pizza: ")
            print("----------------------------------")
        else:
            print("Seleccione una opcion valida")
            continue

        #Print the attributes of the elements on the list
        map(lambda x: print(x.id,' || ',x.nombre,' || ',x.precio),lists)
        for x in lists:
            print(x.id,' || ',x.nombre,' || ',x.precio)

        print("----------------------------------")
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
            Datos.saveIngredient(Datos.Ingrediente(nombre,id,precio))
            print()

        elif(answer == "T" or answer == "t"):
            Datos.saveSize(Datos.Tamano(nombre,id,precio))
            print()
        else:
            print("Seleccione una opcion valida")
            continue

        print("")
        input("Producto agregado, presione cualquier tecla para continuar")
        break


def deleteProduct():
    print()

def modifyProduct():
    print("En construccion")

def exit():
    os.system('clear')
    while True:
        answer = input("Seguro que desea salir? [s/n]: ")

        if (answer == 's' or answer == 'S'):
            print("Hasta luego")
            quit()
        elif (answer == 'n' or answer == 'N'):
            break
        else:
            print("Seleccione una opcion valida")

#Main
switcher = {
        1: viewProducts,
        2: addProduct,
        3: deleteProduct,
        4: modifyProduct,
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
    print("4: Modificar un producto")
    print("0: Salir")

    #try:
    func = switcher.get(int(input("Opcion: ")), lambda: "Seleccione una opcion valida")
    os.system('clear')
    func()
    #except:
        #print("Error desconocido")
