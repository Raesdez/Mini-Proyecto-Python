#---------------- Ramón Sosa ------------------
import Clases
import Datos
import datetime #To get the now for the file name

#For working with PDF and convert HTML to PDF
from fpdf import FPDF, HTMLMixin
class HTML2PDF(FPDF, HTMLMixin):
    pass

#---------------- Global Variables ------------------
file_path = "Recibos/"  #The file path
pdf = HTML2PDF()
#---------------------------------------------------

#---------------- Private Methods ------------------

""" This is a function that generates test data"""
def __pizzaList():
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

""" Summary:    It generates and saves the PDF file given a list of pizzas
    Parameters: pizzas_list: the list of the pizzas, file: full file name, now: the date when the public method was called
    Return:     None"""
def __generate_and_save_PDF(pizzas_list,file,now):

    pdf.add_page() #Adds the page to write the info
    fecha = datetime.datetime.today().strftime('%d/%m/%Y') #Get the time and format it

    staticHTML = '''<h1 style="text-align: center;"><span style="color: #800000;"><strong>Pizzer&iacute;a</strong></span></h1>
        <p><strong><span style="color: #800000;">Fecha:&nbsp'''+fecha+''';</span></strong></p>
        <p><strong><span style="color: #800000;">Recibo N:&nbsp'''+now+''';</span></strong></p>
        <p/>
        <hr />
        <h2><span style="color: #800000;">Detalle de la compra:</span></h2>
        <hr />
        '''+__generate_pizza_tables(pizzas_list)+'''
        <h2><span style="color: #800000;"><strong>Total de pizzas: '''+str(len(pizzas_list))+'''</strong></span></h2>
        <h2><span style="color: #800000;"><strong>Total a pagar: '''+str(sum(map(lambda i: i.calcularTotal(),pizzas_list)))+'''</strong></span></h2>
        <hr />
        <p>&nbsp;</p> '''

    pdf.write_html(staticHTML) #Write the html code into the pDF
    pdf.output(file)    #Save the file

""" Summary:    Add each of the ingredients to a pizza's info
    Parameters: ingredient_list: the list of the ingredients on a pizza
    Return:     list: the info of the ingredients"""
def __generateIngredientsListHTML(ingredient_list):
    list = ""
    for ingredient in ingredient_list:
        list += ingredient.id+"("+str(ingredient.precio)+")"+", "
    return list

""" Summary:    Creates the portion of the pdf that contains the table with the pizzas' info
    Parameters: pizzas_list: the list of the pizzas
    Return:     table: full constructed pizzas table"""
def __generate_pizza_tables(pizzas_list):
    pizzas_info = ""

    #Place the pizza info in each row of the table
    for pizza in pizzas_list:
        pizzas_info = pizzas_info+'''<tr>
                            <td>'''+str(pizza.numero)+'''</td>
                            <td>'''+str(pizza.tamano.nombre)+''' ('''+str(pizza.tamano.precio)+''')</td>
                            <td>'''+str(__generateIngredientsListHTML(pizza.ingredientes))+'''</td>
                            <td>'''+str(pizza.calcularTotal())+'''</td>
                        </tr>'''

    table = '''<table border="1" align="right" width="100%">
                <thead>
                    <tr>
                        <th width="5%">N</th>
                        <th width="20%">Tamano</th>
                        <th width="60%">Ingredientes</th>
                        <th width="15%">Subtotal</th>
                    </tr>
                </thead>
                <tbody>
                '''+pizzas_info+'''
                </tbody>
                </table>
             '''
    return table
#------------------------------------------------------------------------------

#---------------- Public Method -----------------------------------------------
""" Summary:    Called from the Client to generate the PDF
    Parameters: pizzas_list: the list of the pizzas
    Return:     0: PDF created succefully, 9: unexpected error"""
def generate_receipt(pizzas_list=[]):
    try:
        now = str(datetime.datetime.now())      #Get the now when the function is called
        file = file_path+"Recibo"+now+".pdf"    #Give a name to the file
        __generate_and_save_PDF(pizzas_list,file,now)      #Generate and saves PDF
        return 0
    except:
        return 9

#------------------------------------------------------------------------------

if __name__ == '__main__':
    generate_receipt(__pizzaList())
