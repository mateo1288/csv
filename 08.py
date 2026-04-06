import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")

print("Columnas gender y math score:")
print(df[['gender', 'math score']])

print("Tipo de dato de gender:")
print(df['gender'].dtype)

print("Valores nulos por columna:")
print(df.isnull().sum())

print("Filas y columnas:")
print(df.shape)

print("Últimas 5 filas:")
print(df.tail(5))