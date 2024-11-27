import pandas as pd

df = pd.DataFrame({
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [20, 25, 22, 27]
})

print("df:", df)


df_pivot = df.pivot(index='Date', columns='City', values='Temperature')
print(df_pivot)