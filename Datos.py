#---------------- Ramón Sosa ------------------

#Import classes
from Clases import Ingrediente,Tamano
from functools import reduce
#Import library for storing objects in files
import pickle

#----------- Global Variables --------------------
ingredientsFile = "ingredientes"
sizesFile = "tamanos"
#---------------------------------------------------


#-------------------------- Private methods -------------------------------
""" Summary:    Stores an object in the stated file
    Parameters: new_object: the object to be stored, file_name: the name of the file
    Return:     0: if store success, 1: object id is duplicated, 9:unexpected error"""
def __saveObject(new_object,file_name):
    try:
        #Get stored list
        list = listOfObjects(file_name)

        #Check if the id is already on the list
        if(not isIdDuplicated(list,new_object)):
            #Append the new object to the list
            list.append(new_object)
            #Open file and save the list
            with open(file_name, 'wb') as file:
                pickle.dump(list,file)
        else:
            return 1 #Object id is duplicated
    except:
        return 9

""" Summary:    Reads the file and return a list of the objects in that file
    Parameters: file_name: the name of the file
    Return:     object list or [] if an error ocurred"""
def __listOfObjects(file_name):
    try:
        with open(file_name,'rb') as file:
            list = pickle.load(file)
    except:
        list = []
    return list

def __eliminateObject(object,file_name):
    # try:
         #Get stored list
         lists = listOfObjects(file_name)

         #Apply filter to generate a list with the objects that dont have the object id
         lists = list(filter(lambda x: x.id != object.id,lists))
         print("La lista que cumplió la condición",lists)

         #Open file and save the list
         with open(file_name, 'wb') as file:
                 pickle.dump(lists,file)

     #except:
    #     return 9

""" Summary:    Checks if the id of the new object exist in the file
    Parameters: list: the list of objects, new_object: the new object to check if exists
    Return:     True: if it is duplicated , False: if not exists on the list"""
def __isIdDuplicated(list,new_object):
    for object in list:
        if object.id == new_object.id:
            return True

    return False

#---------------------------------------------------------------------------

#----------------------- Public Service Methods ---------------------

def saveIngredient(new_ingredient):
    return saveObject(new_ingredient,ingredientsFile)

def ingredientsList():
    return listOfObjects(ingredientsFile)

def saveSize(new_size):
    return saveObject(new_size,sizesFile)

def sizesList():
    return listOfObjects(sizesFile)

#---------------------------------------------------------------------------

def imprimirIngredientes(lista):
    i = 0
    for ingrediente in lista:
        i+=1
        print(i,": ",ingrediente.id,", ",ingrediente.nombre,", ",ingrediente.precio)


ingrediente = Ingrediente("","",0.00)
ingrediente.nombre = str(input('Indique el nombre del producto: '))
ingrediente.id = str(input('Indique el codigo del producto: '))
ingrediente.precio = float(input('Indique el precio del producto: '))
print("")

if (saveIngredient(ingrediente) == 1):
    print("Ya existe este ingrediente")
else:
    print("La lista de productos actuales")
    imprimirIngredientes(ingredientsList())
    print("Eliminando ",ingrediente.nombre)
    eliminateObject(ingrediente,ingredientsFile)
    imprimirIngredientes(ingredientsList())

#print("Total de precio de los productos",reduce((lambda x, y: x + y),map(lambda x: x.precio, ingredientsList())))
