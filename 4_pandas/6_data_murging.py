import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

# sample file conversion
# sample_data = pd.read_csv('files/youth_unemployed.csv')
# sample_data.to_html('files/youth_unemployed.html')

country = pd.read_csv('files/youth_unemployment.csv', index_col=0)
df = country.head(5)
df = df.set_index('Country Code')
sd = df.reindex(columns=['2011', '2012'])
db = sd.diff(axis=1)
db.plot(kind='bar')
plt.show()
