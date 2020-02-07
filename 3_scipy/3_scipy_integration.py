from scipy import integrate
from scipy import special

# print(help(integrate.quad))

# single integration
i = integrate.quad(lambda x: special.exp10(x), 0, 1)
print(i)

# double integration
e = lambda x, y: x * y ** 2
f = lambda x: 1
g = lambda x: -1
print(integrate.dblquad(e, 0, 2, f, g))
