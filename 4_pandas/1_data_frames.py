import pandas as pd

xyz_web = {
    'Day': [1, 2, 3, 4, 5, 6],
    'Visitors': [1000, 2000, 1400, 900, 800, 110],
    'Bounce_Rate': [20, 30, 22, 21, 18, 16]
}
df = pd.DataFrame(xyz_web)
# print(df)

# slicing first 2 rows
print(df.head(2))

# last 2 rows
print(df.tail(3))
