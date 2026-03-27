import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
df[df.columns[:3]].head(10)