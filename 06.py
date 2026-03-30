import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Primeras 100 filas:")
print(df.head(100))

print("Cantidad de filas y columnas:")
print(df.shape)

print("Última fila:")
print(df.tail(1))