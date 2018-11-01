#---------------- Ramón Sosa ------------------
import os
import Datos
#Clean screem
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")

""" Summary: Prints a list of selected products"""
def __view_products():
    while True:
        answer = input("Indique el tipo de producto que desea consultar (i: ingrediente, t: tamano): ")
        print("")
        if(answer == "I" or answer == "i"):
            lists = Datos.ingredients_list()
            print("Mostrando todos los ingredientes: ")
        elif(answer == "T" or answer == "t"):
            lists = Datos.sizes_list()
            print("Mostrando todos los tamanos de pizza: ")
        else:
            print("Seleccione una opcion valida")
            continue

        __print_list(lists)
        print("")
        input("Presione cualquier tecla para volver")
        break

""" Summary: Adds a product using the Datos based on the info provided"""
def __add_product():
    while True:
        answer = input("Indique el tipo de producto que desea agregar (i: ingrediente, t: tamano): ")

        #Constructing the object
        nombre = str(input('Indique el nombre del producto: '))
        id = str(input('Indique el codigo del producto: '))
        precio = float(input('Indique el precio del producto: '))

        if(answer == "I" or answer == "i"):
            if(Datos.save_ingredient(Datos.Ingrediente(id,nombre,precio))==1):
                print("Ya existe un ingrediente con este identificador, por favor intente nuevamente")
                continue
            print()

        elif(answer == "T" or answer == "t"):
            if(Datos.save_size(Datos.Tamano(id,nombre,precio))):
                print("Ya existe un tamano con este identificador, por favor intente nuevamente")
                continue
            print()
        else:
            print("Seleccione una opcion valida")
            continue

        print("")
        input("Producto agregado, presione cualquier tecla para continuar")
        break

""" Summary: Deletes a selected product"""
def __delete_product():
    while True:
        answer = input("Indique el tipo de producto que desea eliminar (i: ingrediente, t: tamano): ")
        print("")
        #Set the function and the list to be shown based on the choice
        if(answer == "I" or answer == "i"):
            lists = Datos.ingredients_list()
            func = Datos.delete_ingredient
            print("Mostrando todos los ingredientes: ")
        elif(answer == "T" or answer == "t"):
            lists = Datos.sizes_list()
            func = Datos.delete_size
            print("Mostrando todos los tamanos de pizza: ")
        else:
            print("Seleccione una opcion valida")
            continue

        #Print the list
        __print_list(lists)
        print("")

        #Delete the selected object or ask again if input was wrong
        id = input("Indique el Id del producto a eliminar: ")
        product = __search_by_id(lists,id)
        if(product != None):
            func(product)
        else:
            print("Seleccione una opcion valida")
            continue

        input("Producto eliminado, presione cualquier tecla para continuar: ")
        break

""" Summary: terminates the program after users confirmation"""
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
""" Summary: Prints a list of products
    Parameters: lists: list of objects (Tamano, Ingrediente)"""
def __print_list(lists):
    print("----------------------------------")
    i = 0
    for x in lists:
        i+= 1
        print(i,":",x.id,',',x.nombre,',',x.precio)
    print("----------------------------------")

""" Summary: Given a list of ingredients or sizes it returns the one whos id matched
    Parameters: lists: the list with the objects, id: the id that needs to be matched
    Return:     product: the object whos id matched, None: is no product id matched"""
def __search_by_id(lists,id):
    for product in lists:
        if product.id == id:
            return product
    return None
#-------------------------  Main  ---------------------------------
switcher = {
        1: __view_products,
        2: __add_product,
        3: __delete_product,
        0: exit,
    }

while True:

    clear()
    print("------------------------------------------")
    print("Bienvenido al Administrador de la Pizzeria UCAB")
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
    clear()
    func()
    #except:
        #print("Error desconocido")
