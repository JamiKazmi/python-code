import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# changing style
sns.set(style='darkgrid')

a = sns.load_dataset('flights')
b = sns.PairGrid(a)
b.map(plt.scatter)
plt.show()
