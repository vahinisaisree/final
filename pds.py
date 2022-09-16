from fpdf import FPDF  # importing FPDF for generating pdf
import os  # importing os for opening of pdf directly


def pdf_file():
    # creating a pdf and adding a page
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=13)

    f = open("vahini.txt", "r")  # taking text file to print text in pdf
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='L')
    # output pdf
    pdf.output("my.pdf")
    os.system('my.pdf')

