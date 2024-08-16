# cspell: disable
import pandas as pd
import random
import faker

# Inicializar el generador de datos falsos
fake = faker.Faker()

# Número de registros que queremos generar
num_registros = 10

# Crear una lista de diccionarios con datos aleatorios
data = []
for _ in range(num_registros):
    registro = {
        "U.R.": "600 -->SUBSECRETARÍA DE EDUCACIÓN MEDIA SUPERIOR",
        "Programa": fake.job(),
        "Oficio de afectación presupuestal": fake.bothify(text='OFICIO-####'),
        "CURP": fake.bothify(text='????######????###'),
        "RFC y Homoclave": fake.bothify(text='???######'),
        "Primer apellido": fake.last_name(),
        "Nombre(s)": fake.first_name() + ' ' + fake.last_name(),
        "Nacionalidad": "MEXICANA",
        "Sexo": random.choice(["MASCULINO", "FEMENINO"]),
        "Escolaridad": random.choice(["LICENCIATURA", "MAESTRÍA", "DOCTORADO"]),
        "Estado de Nacimiento": fake.state(),
        "Especifique": fake.random_number(digits=8),
        "Banco o CLABE": fake.company(),
        "CLABE": fake.bothify(text='#########'),
        "Fecha de inicio del contrato": fake.date_this_decade().strftime('%Y-%m-%d') + ' -->ENERO',
        "Fecha de término del contrato": fake.date_this_decade().strftime('%Y-%m-%d') + ' -->FEBRERO',
        "Nivel del Contrato": fake.word() + ' -->ENLACE',
        "Monto Bruto Mensual": fake.random_number(digits=5),
        "Fina": "FISCALES",
        "Compatibilidad": random.choice([True, False]),
        "Conocimientos requeridos por la dependencia": fake.text(max_nb_chars=50)
    }
    data.append(registro)

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Guardar el DataFrame a un archivo Excel
df.to_excel('datos_aleatorios.xlsx', index=False)

print("Archivo Excel creado con 10 registros aleatorios.")
