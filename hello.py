print("Hello world!")

print(6+4*10)

print((6+4)*10)

import math
print(math.pow(23,5))

import cmath
a = 34
b = 68
c = 510

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

