from exceptions import Empty

class Queue:
    def __init__(self):
        # to do
        self._data = []

    def __len__(self):
        # to do
        return len(self._data)

    def is_empty(self):
        # to do
        return self.__len__() == 0

    def enqueue(self, e):
        # to do
        self._data.append(e)

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        # to do
        to_return = self._data.pop(0)
        return to_return
    
    def front(self):
        if self.is_empty():
          raise Empty('Queue is empty')
        # to do
        return self._data[0]

    def __repr__(self):
        return str(self._data)


queue2 = Queue()

queue2.enqueue(2)
queue2.enqueue(8)
queue2.enqueue(16)
queue2.enqueue(32)
queue2.enqueue(64)

print(queue2)

print(queue2.dequeue())
print(queue2.dequeue())
print(queue2.dequeue())

print(queue2)
