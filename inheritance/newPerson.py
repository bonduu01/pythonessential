class Person:
    def __init__(self, weight, age, salary):
        self.weight = weight
        self.age = age
        self.salary = salary

    def __add__(self, new_weight):
        return self.weight + new_weight.weight


person1 = Person(80, 35, 50000)
person2 = Person(70, 26, 10000)

print(person1 + person2)
