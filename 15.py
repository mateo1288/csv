import pandas as pd

df = pd.read_csv("archivo.csv")

print(df[['pais', 'edad']])

print(df.sort_values('edad'))

print(df[df['pais'] == 'Alemania'].head(5))