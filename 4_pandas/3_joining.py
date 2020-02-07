import pandas as pd

df1 = pd.DataFrame(
    {
        'Int_Rate': [2, 3, 1, 2],
        'IND_GDP': [40, 50, 80, 65]
    },
    index=[2001, 2002, 2003, 2004]
)
df2 = pd.DataFrame(
    {
        'Low_Tier_HPI': [50, 46, 43, 38],
        'Unemployment': [1, 2, 2, 4]
    },
    index=[2001, 2003, 2004, 2005]
)
joined = df1.join(df2)
print(joined)
