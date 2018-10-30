import Clases
import Datos
import datetime
from fpdf import FPDF

#The file name
file = "Recibos/Recibo"+str(datetime.datetime.now())+".pdf"
pdf = FPDF()

""" """
def __simple_table(spacing=1,lists=[]):
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font("Arial", size=12)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in lists:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

def __generateListsToPrint(pizzas_list):
    data = [['Numero', 'Tamano', 'Ingredientes','Precio']]

    for pizza in pizzas_list:
        ingredient_list = ""
        for ingredient in pizza.ingredientes:
            ingredient_list += ingredient.nombre+", "
        data.append([str(pizza.numero),pizza.tamano.nombre,ingredient_list,str(pizza.calcularTotal())])

    __simple_table(1,data)

def pizzaList():
    #Pizza 1
    pizza1 = Clases.Pizza(1)
    pizza1.ingredientes.append(Datos.ingredientsList()[0])
    pizza1.ingredientes.append(Datos.ingredientsList()[1])
    pizza1.ingredientes.append(Datos.ingredientsList()[2])
    pizza1.ingredientes.append(Datos.ingredientsList()[0])
    pizza1.tamano = Datos.sizesList()[0]
    #Pizza 2
    pizza2 = Clases.Pizza(2)
    pizza2.ingredientes.append(Datos.ingredientsList()[1])
    pizza2.ingredientes.append(Datos.ingredientsList()[2])
    pizza2.tamano = Datos.sizesList()[0]

    list = []

    list.append(pizza1)
    list.append(pizza2)
    return list


def generateReceipt(pizzas_list=[]):
    pdf.add_page()
    list = pizzaList()
    __generateListsToPrint(list)
    pdf.output(file)

if __name__ == '__main__':
    generateReceipt()
