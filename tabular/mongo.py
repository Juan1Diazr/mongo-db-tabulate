from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Conectar a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["EJERCICIO"]
collection = db["datal"]

# Recuperar datos de la colección
datos = list(collection.find())

# Convertir los datos en un DataFrame de pandas
df = pd.DataFrame(datos)

# Verificar que el DataFrame tenga datos
if df.empty:
    print("No se encontraron datos en la colección.")
else:
    # Mostrar la tabla con formato
    print("Datos recuperados de MongoDB:")
    print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    # Configuración de la gráfica (usar columnas relevantes)
    plt.figure(figsize=(12, 6))
    sns.barplot(x="DEPARTAMENTO", y="CANTIDAD", data=df, palette="viridis")
    plt.title("Cantidad por Departamento", fontsize=16)
    plt.xlabel("Departamento", fontsize=12)
    plt.ylabel("Cantidad", fontsize=12)
    plt.xticks(rotation=45, ha="right")  # Rotar etiquetas para mejor lectura
    plt.tight_layout()  # Ajusta la gráfica para que no se corte el texto
    plt.show()
