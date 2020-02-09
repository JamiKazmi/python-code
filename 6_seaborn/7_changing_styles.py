import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# changing style is very easy in seaborn
sns.set(style='white', color_codes=True)

a = sns.load_dataset('tips')
sns.boxenplot(x='day', y='total_bill', data=a)
sns.despine(offset=10, trim=True)

c = sns.color_palette()
sns.palplot(c)

plt.show()
