import os
import PyPDF2
from tkinter import Tk, Label, Button, filedialog
import modelo

# Interfaz gráfica
    
def crear_interfaz(root):
    root.title("Unir PDFs")
    root.geometry("400x200")

    etiqueta = Label(root, text="Seleccione los archivos PDF a unir:")
    etiqueta.pack(pady=10)

    # Botón para unir y descargar
    boton_unir_descargar = Button(root, text="Unir y Descargar", command=unir_y_descargar)
    boton_unir_descargar.pack(pady=10)

    root.mainloop()

def unir_y_descargar():
    create_table()
    archivos_seleccionados = seleccionar_archivos()
    if archivos_seleccionados:
        archivo_salida = "pdf_unidos.pdf"
        unir_pdfs(archivos_seleccionados, archivo_salida)
        descargar_archivo(archivo_salida)    

    root.mainloop()





