from math import pi
from math import sin
import math

print(sin(pi / 2))
print(math.sin(math.pi / 2))

print(sorted(dir(math)))

from math import ceil, floor, trunc, factorial

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

x = 3
print(factorial(x))