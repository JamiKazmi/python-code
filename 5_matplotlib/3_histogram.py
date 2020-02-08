import matplotlib.pyplot as plt

population_ages = [
    22, 55, 126, 34, 45, 8, 113, 23, 45, 87, 99, 111, 76, 67,
    77, 119, 39, 110, 66, 123
]
bins = [
    0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130
]
plt.hist(
    population_ages,
    bins, histtype='bar',
    rwidth=0.8
)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Histogram')
plt.legend()
plt.show()
