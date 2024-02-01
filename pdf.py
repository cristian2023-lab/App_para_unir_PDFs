import os
import PyPDF2
from tkinter import Tk, Label, Button, filedialog
import sqlite3
from datetime import datetime

# Conexión a la base de datos SQLite
def conexion():
    conexion_pdf = sqlite3.connect('pdf.db')
    return conexion_pdf

def create_table():
    conn = sqlite3.connect('pdf.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pdf (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            fecha_descarga TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Funciones de manipulación de PDFs
def unir_pdfs(lista_archivos, archivo_salida):
    merger = PyPDF2.PdfMerger()
    for archivo in lista_archivos:
        merger.append(archivo)
    merger.write(archivo_salida)
    merger.close()

def seleccionar_archivos():
    archivos = filedialog.askopenfilenames(title="Seleccionar archivos PDF", filetypes=[("Archivos PDF", "*.pdf")])
    return archivos

def descargar_archivo(archivo):
    os.startfile(archivo)

# Interfaz gráfica
    
def crear_interfaz():
    root = Tk()
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

# Llamamos a la función principal para crear la interfaz
crear_interfaz()
