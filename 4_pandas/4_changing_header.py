import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

df = pd.DataFrame({
    'Day': [1, 2, 3, 4],
    'Visitors': [200, 100, 230, 300],
    'Bounce_Rate': [20, 40, 60, 10]
})
df = df.rename(columns={'Visitors': 'Users'})
print(df)

# df.set_index('Day', inplace=True)
# df.plot()
# plt.show()
