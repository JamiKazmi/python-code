import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

b = sns.load_dataset('tips')
# scattered
sns.catplot(x='day', y='total_bill', data=b)
# violin type
sns.catplot(x='day', y='total_bill', kind='violin', data=b)
# boxen
sns.catplot(x='day', y='total_bill', kind='boxen', data=b)

plt.show()
