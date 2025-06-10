from random import random, randrange, randint, choice, sample

for i in range(5):
    print(random())
print("-------------------------------------")
from random import seed

seed(1)
for i in range(5):
    print(random())
print("-------------------------------------")

print(randrange(100), end=' ')
print(randrange(0, 100), end=' ')
print(randrange(0, 100, 1), end=' ')
print(randint(0, 100))
print("-------------------------------------")

for i in range(5):
    print(randint(i + 1, 10 - i), end = ' ')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 9))
print(sample(my_list, 10))