import pandas as pd

df = pd.read_excel('input1.xlsx')

df.to_excel('input1.xlsx', index=False)

print(df)