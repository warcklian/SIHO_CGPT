# cspell: disable
import pandas as pd
import random

# Generación de datos de ejemplo
first_names = ["Juan", "María", "Pedro", "Ana", "Luis", "Carmen", "José", "Lucía", "Carlos", "Laura"]
last_names = ["García", "Martínez", "Rodríguez", "López", "González", "Pérez", "Sánchez", "Ramírez", "Hernández", "Flores"]

data = {
    "First Name": [random.choice(first_names) for _ in range(20)],
    "Last Name (Paternal)": [random.choice(last_names) for _ in range(20)],
    "Last Name (Maternal)": [random.choice(last_names) for _ in range(20)],
    "RFC": ["".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=13)) for _ in range(20)],
    "Address": [f"Street {random.randint(1, 100)} #{random.randint(1, 1000)}" for _ in range(20)],
    "Postal Code": [f"{random.randint(10000, 99999)}" for _ in range(20)],
    "Phone": [f"55{random.randint(10000000, 99999999)}" for _ in range(20)],
    "Email": [f"email{random.randint(1, 1000)}@example.com" for _ in range(20)]
}

# Creación del DataFrame y guardado en un archivo Excel
df = pd.DataFrame(data)
df.to_excel("data.xlsx", index=False)
