class Queue:
    def __init__(self, size=100):
        self._arraySize = size
        self._array = [None]*size
        self._objCount = 0
        self._rear = 0
        self._front = 0

    def size(self):
        return self._objCount

    def isEmpty(self):
        return self.size() == 0

    def isFull(self):
        return self.size() == self._arraySize

    def insert(self, val):
        if not self.isFull():
            self._array[self._rear] = val
            self._rear = self._rear + 1
            self._objCount = self._objCount + 1
        else:
            raise RuntimeError("queue full")

    def peek(self):
        if not self.isEmpty():
            return self._array[self._front]
        else:
            raise RuntimeError("queue empty, nothing to return")

    def remove(self):
        val = self.peek()
        self._front = self._front + 1
        self._objCount = self._objCount - 1
        return val

def main():
    q = Queue(25)
    print(q.isEmpty())
    print(q.size())
    q.insert(20)
    print(q.size())
    q.insert(50)
    print(q.size())
    q.insert(10)
    print(q.size())
    print(q.isEmpty())
    print(q.size())
    print(q.remove())
    print(q.remove())
    print(q.remove())
    q.insert(50)
    q.insert(10)
    print(q.size())
    print(q.remove())
    print(q.remove())
    print(q.remove())    # comment this line
    print(q.isEmpty())

main()