import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Columnas del dataset:")
print(df.columns)

print("Columnas gender y math score:")
print(df[['gender', 'math score']])

print("Filas y columnas:")
print(df.shape)

print("Primeras 4 filas:")
print(df.head(4))

print("Últimas 4 filas:")
print(df.tail(4))