import Clases
import Datos
from fpdf import FPDF

#The file name
file = "Recibo.pdf"

def simple_table(spacing=1):

    lists = Datos.ingredientsList()

    data = [['Id', 'Nombre', 'Precio']]
    for ingredient in lists:
        data.append([ingredient.id,ingredient.nombre,str(ingredient.precio)])


    pdf.set_draw_color(0, 0, 0)
    pdf.set_font("Arial", size=12)
    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

def draw_lines():
    pdf.line(10, 10, 10, 100)
    pdf.set_line_width(1)
    pdf.set_draw_color(255, 0, 0)
    pdf.line(20, 20, 100, 20)

pdf = FPDF()
pdf.add_page()
draw_lines()
simple_table()
draw_lines()
pdf.output(file)