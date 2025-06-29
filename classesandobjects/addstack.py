from stack import push, pop


class AddStack(Stack):
    def __init__(self):
        super.__init__()
        print("Adding Stack example: ")

    def add_stack(self, stack):
        self.__stack_list = stack
        result = sum(stack)
        return result


new_stack = [n for n in range(101)]
addstack = AddStack()
sum_of_stack = addstack.add_stack(new_stack)
print(sum_of_stack)

pushstack = AddStack()
pushstack.st
