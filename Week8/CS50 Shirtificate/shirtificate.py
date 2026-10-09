from fpdf import FPDF


name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

pdf.set_font("helvetica", size=36)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=15, y=60, w=180)

pdf.set_font("helvetica", size=24)
pdf.set_text_color(255, 255, 255)
pdf.set_y(140)
pdf.cell(0, 10, name, align="C")

pdf.output("shirtificate.pdf")