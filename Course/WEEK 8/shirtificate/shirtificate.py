from fpdf import FPDF

class Shirt:
    def create(user_input):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font('helvetica', size=25)
        pdf.cell(80)
        pdf.cell(30, 10, "CS50 Shirtificate", align="C")
        pdf.image("shirtificate.png", 17, 55, 180, 0, "")
        pdf.set_text_color(255, 255, 255)
        pdf.cell(-20, 190, user_input, align="C")
        pdf.output("shirtificate.pdf")

def main():
    user_input = str(input("Enter: "))
    Shirt.create(user_input)






if __name__ == "__main__":
    main()