class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0,elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError()
        val = self.__queue[-1]
        del self.__queue[-1]
        return val

class SuperQueue(Queue): 
    # Write new code here. 
    def __init__(self):
        super().__init__()
    
    def isempty(self):
        return not bool(len(self.__queue))


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False) 
for i in range(4): 
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty") 