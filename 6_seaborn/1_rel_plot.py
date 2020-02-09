import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# scattered
a = sns.load_dataset('flights')
sns.relplot(x='passengers', y='month', hue='year', data=a)
# line
b = sns.load_dataset('tips')
sns.relplot(x='time', y='tip', data=b, kind='line')

plt.show()
