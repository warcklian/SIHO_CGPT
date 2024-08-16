import os
import subprocesing
import sys
import zipfile
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Función para instalar paquetes si no están instalados
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Verificar e instalar las librerías necesarias
required_packages = ['requests', 'pandas', 'selenium', 'openpyxl']
for package in required_packages:
    install_package(package)

# Función para ejecutar el comando npm run find y capturar su salida
def run_npm_find():
    result = subprocess.run(['npm', 'run', 'find'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error ejecutando npm run find: {result.stderr}")
        sys.exit(1)
    return result.stdout

# Función para extraer la URL del ChromeDriver de la salida del comando npm run find
def extract_chromedriver_url(output):
    lines = output.splitlines()
    for line in lines:
        if 'chromedriver-' in line and line.endswith('.zip 200'):
            # Extraer la URL antes del código de estado 200
            return line.split(' ')[0]
    raise Exception("No se encontró una URL válida para ChromeDriver en la salida del comando npm run find.")

# Descargar y extraer ChromeDriver desde la URL proporcionada
def download_and_extract_chromedriver(url):
    chromedriver_zip = 'chromedriver.zip'
    with requests.get(url) as r:
        with open(chromedriver_zip, 'wb') as f:
            f.write(r.content)
    # Extraer el ChromeDriver
    with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
        zip_ref.extractall()
    # Limpiar el archivo zip
    os.remove(chromedriver_zip)

# Ejecutar el comando npm run find y capturar su salida
npm_output = run_npm_find()

# Extraer la URL del ChromeDriver desde la salida
chromedriver_url = extract_chromedriver_url(npm_output)

# Descargar y extraer ChromeDriver
download_and_extract_chromedriver(chromedriver_url)

# Leer el archivo Excel
df = pd.read_excel('datos.xlsx', engine='openpyxl')

# Configurar el navegador utilizando el ChromeDriver descargado
driver = webdriver.Chrome(executable_path="./chromedriver")

# URL de la página web donde se ingresarán los datos
url = "https://www.ejemplo.com/formulario"
driver.get(url)

# Iterar sobre cada fila del DataFrame y llenar el formulario
for index, row in df.iterrows():
    # Rellenar los campos del formulario con los datos del Excel
    driver.find_element(By.NAME, "nombre").send_keys(row['Nombre'])
    driver.find_element(By.NAME, "apellido_paterno").send_keys(row['Apellido Paterno'])
    driver.find_element(By.NAME, "apellido_materno").send_keys(row['Apellido Materno'])
    driver.find_element(By.NAME, "rfc").send_keys(row['RFC'])
    driver.find_element(By.NAME, "domicilio").send_keys(row['Domicilio'])
    driver.find_element(By.NAME, "codigo_postal").send_keys(row['Código Postal'])
    driver.find_element(By.NAME, "telefono").send_keys(row['Teléfono'])
    driver.find_element(By.NAME, "correo").send_keys(row['Correo Electrónico'])
    
    # Enviar el formulario (esto depende de cómo esté implementado en la página)
    driver.find_element(By.NAME, "submit_button").click()
    
    # Esperar un poco para evitar enviar datos demasiado rápido
    time.sleep(2)
    
    # Regresar a la página para llenar el siguiente formulario (esto depende de cómo esté implementado en la página)
    driver.get(url)

# Cerrar el navegador al finalizar
driver.quit()
