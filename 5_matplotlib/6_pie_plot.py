import matplotlib.pyplot as plt

slices = [7, 2, 3, 13]
activities = [
    'sleeping',
    'eating',
    'working',
    'playing'
]
cols = ['c', 'm', 'r', 'b']

plt.pie(
    slices,
    labels=activities,
    startangle=90,
    shadow=True,
    explode=(0, 0.1, 0, 0),
    autopct='%1.1f%%'
)
plt.title('Pie Chart')
plt.legend()
plt.show()
