from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class EstrategiaFormato:
    def salvar(self, file, contenido):
        raise NotImplementedError("Debe implementarse en una subclase.")


# Estrategia para pdf
class PDF(EstrategiaFormato):
    def salvar(self, file, contenido):
        pdf_file = f"{file}.pdf"
        c = canvas.Canvas(pdf_file, pagesize=letter)
        ancho, alto = letter
        y = alto - 100
        for linea in contenido.split('\n'):
            c.drawString(100, y, linea)
            y -= 15
            if y < 50:
                c.showPage()
                y = alto - 100
        c.save()
        print(f"Se ha guardado en PDF: {pdf_file}")


# Estrategia para docx
class Doc(EstrategiaFormato):
    def salvar(self, file, contenido):
        doc_file = f"{file}.docx"
        doc = Document()
        doc.add_paragraph(contenido)
        doc.save(doc_file)
        print(f"Se ha guardado en DOCX: {doc_file}")

# Estrategia para txt
class Text(EstrategiaFormato):
    def salvar(self, file, contenido):
        txt_file = f"{file}.txt"
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write(contenido)
        print(f"Se ha guardado en TXT: {txt_file}")


class Archivo:
    def __init__(self, formato):
        self.formato = formato
        self.contenido = ""

    def texto(self, texto):
        self.contenido = texto

    def set_formato(self, formato):
        self.formato = formato

    def salvar(self, nombre):
        self.formato.salvar(nombre, self.contenido)


if __name__ == "__main__":
    p = PDF()
    d = Doc()
    t = Text()

    a = Archivo(p)
    a.texto("Hello da, esto es un texto el cual se va a convertir en diferentes formatos.")

    a.salvar("hola_pdf")   
    a.set_formato(d)
    a.salvar("hola_doc")  
    a.set_formato(t)
    a.salvar("hola_texto") 
