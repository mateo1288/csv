import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Últimas 3 columnas:")
print(df[df.columns[-3:]])

print("Primeras 100 filas:")
print(df.head(100))

print("Cantidad de la primera columna:")
print(df[df.columns[0]].count())

print("Filas vacías:")
print(df.isnull().any(axis=1).sum())

print("Tipos de datos:")
print(df.dtypes)