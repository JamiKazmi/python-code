import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# multivariate distribution
x = pd.DataFrame({
    'Day': [1, 2, 3, 4, 5, 6, 7],
    'Grocery': [30, 80, 45, 40, 65, 90, 87],
    'Clothes': [45, 13, 68, 97, 67, 85, 72],
    'Utensils': [12, 14, 78, 91, 76, 65, 78]
})
y = pd.DataFrame({
    'Day': [8, 9, 10, 11, 12, 13, 14],
    'Grocery': [30, 80, 45, 40, 65, 90, 87],
    'Clothes': [45, 13, 68, 97, 67, 85, 72],
    'Utensils': [12, 14, 78, 91, 76, 65, 78]
})
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
with sns.axes_style('white'):
    sns.jointplot(x=x, y=y, kind='kde', color='b')

plt.show()
