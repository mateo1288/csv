import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

columnas = df.columns[:-1]
print("Todas las columnas menos la última:")
print(df[columnas])

print("Primeras 7 filas:")
print(df.head(7))

print("Filas y columnas:")
print(df.shape)

print("Cantidad de filas:")
print(len(df))

print("Tipos de datos:")
print(df.dtypes)

print("Últimas 2 filas:")
print(df.tail(2))