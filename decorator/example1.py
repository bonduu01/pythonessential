"""A decorator in Python is a powerful and elegant way to modify or enhance the behavior of functions or methods without
 changing their actual code. """


def simple_decorator(function):
    print('We are about to call "{}"'.format(function.__name__))
    return function


def simple_hello():
    print("Hello from simple function!")


# simple_hello()
decorated = simple_decorator(simple_hello)
decorated()
