import sqlite3
from datetime import datetime
import os

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

def unir_y_descargar():
    create_table()
    archivos_seleccionados = seleccionar_archivos()
    if archivos_seleccionados:
        archivo_salida = "pdf_unidos.pdf"
        unir_pdfs(archivos_seleccionados, archivo_salida)
        descargar_archivo(archivo_salida)