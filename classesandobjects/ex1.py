stack = [i for i in range(10)]


def push(val):
    stack.append(val)
    print(stack)


def pop():
    val = stack[-1]
    del stack[-1]
    # sorted(stack)
    return val


push(len(stack))
print(pop())
print(stack)

# push(10)
# push(11)
#
# print(pop())
# print(pop())
# print(pop())
