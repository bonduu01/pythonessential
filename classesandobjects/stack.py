class Stack:
    def __init__(self):
        # print("Hi!")
        self.__stack_list = []

    def push(self, val, stack):
        self.__stack_list = stack
        self.__stack_list.append(val)
        return self.__stack_list

    def pop(self, stack):
        self.__stack_list = stack
        removed_num = self.__stack_list[-1]
        del self.__stack_list[removed_num]
        return self.__stack_list


new_stack = [i for i in range(10)]

newClass = Stack()
anotherClass = Stack()
thirdClass = Stack()

new_stack = newClass.push(len(new_stack), new_stack)
print(new_stack)

new_stack = newClass.pop(new_stack)
print(new_stack)

for i in range(3):
    new_stack = newClass.pop(new_stack)
print(new_stack)

for i in range(11):
    if i not in new_stack:
        anotherClass.push(i, new_stack)
print(new_stack)

thirdClass.push(len(new_stack), new_stack)
print(new_stack)
