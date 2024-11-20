import PyPDF2
import sys

# Función para combinar PDFs
def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(f"Agregando {pdf}...")
        merger.append(pdf)
    merger.write('super.pdf')
    merger.close()

# Combinar los PDFs proporcionados como argumentos
inputs = sys.argv[1:]
if len(inputs) > 1:
    pdf_combiner(inputs)
else:
    print("Por favor, proporciona al menos dos PDFs para combinar.")
    sys.exit()

# Función para agregar una marca de agua
def add_watermark(input_pdf, watermark_pdf, output_pdf):
    with open(input_pdf, 'rb') as base_file, open(watermark_pdf, 'rb') as overlay_file:
        base_reader = PyPDF2.PdfReader(base_file)
        overlay_reader = PyPDF2.PdfReader(overlay_file)
        writer = PyPDF2.PdfWriter()

        # Iterar por cada página del PDF base y aplicar la marca de agua
        for i in range(len(base_reader.pages)):
            base_page = base_reader.pages[i]
            overlay_page = overlay_reader.pages[0]  # Suponemos una sola página de marca de agua
            base_page.merge_page(overlay_page)  # Superponer la marca de agua
            writer.add_page(base_page)

        # Guardar el resultado en el archivo de salida
        with open(output_pdf, 'wb') as output_file:
            writer.write(output_file)

# Aplicar la marca de agua al PDF combinado
try:
    add_watermark('super.pdf', 'wtr.pdf', 'super_wtr.pdf')
    print("PDF combinado con marca de agua generado como 'super_wtr.pdf'.")
except FileNotFoundError as e:
    print(f"Error: {e}. Asegúrate de que los archivos 'super.pdf' y 'wtr.pdf' existan.")
