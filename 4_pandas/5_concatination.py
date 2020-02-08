import pandas as pd

df1 = pd.DataFrame(
    {
        'HPI': [90, 80, 60, 70],
        'Int_Rate': [2, 3, 1, 2],
        'IND_GDP': [40, 50, 80, 65]
    },
    index=[2001, 2002, 2003, 2004]
)
df2 = pd.DataFrame(
    {
        'HPI': [90, 80, 60, 70],
        'Int_Rate': [2, 3, 1, 2],
        'IND_GDP': [40, 50, 80, 65]
    },
    index=[2005, 2006, 2007, 2008]
)

concat = pd.concat([df1, df2])
print(concat)
