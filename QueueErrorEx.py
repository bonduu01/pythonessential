class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__que = []

    def put(self, elem):
        self.__que.append(elem)

    def get(self):
        if len(self.__que) > 0:
            val = self.__que[-1]
            del self.__que[-1]
            return val
        else:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
