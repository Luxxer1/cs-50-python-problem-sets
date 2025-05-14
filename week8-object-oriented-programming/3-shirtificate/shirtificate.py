import sys
from fpdf import FPDF

def main():
    name = input("Name: ")

    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 24)

    title = 'CS50 Shirtificate'
    title_w = pdf.get_string_width(title) + 6

    pdf.set_x((210 - title_w) / 2)
    pdf.cell(title_w, 10, title)

    image_path = 'shirtificate.png'

    try:
        page_width = 210 
        img_width = 120
        x_img = (page_width - img_width) / 2
        y_img = 30

        pdf.image(image_path, x=x_img, y=y_img, w=img_width)
    except RuntimeError:
        sys.exit(f"Could not open image file '{image_path}'")

    pdf.set_font('Helvetica', 'B', 32)
    pdf.set_text_color(255, 255, 255)

    name_w = pdf.get_string_width(name)
    x_name = (page_width - name_w) / 2
    y_name = y_img + img_width * 0.5 - 5

    pdf.set_xy(x_name, y_name)
    pdf.cell(name_w, 10, name)

    pdf.output('shirtificate.pdf')

if __name__ == '__main__':
    main()
