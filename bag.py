class Bag:

    def __init__(self, ARSize = 100):
        self.ARSize=ARSize
        self.BagSize=0
        self.Array=[None]*self.ARSize

    class BagIterator:
        def __init__(self, index=0, list=None):
            self.current = index-1
            self.list = list
        def __next__( self ):
            if self.current != self.list.BagSize-1:
                self.current = self.current + 1
                return self.list.Array[self.current]
            else:
                raise StopIteration

    def __iter__(self):
        return self.BagIterator(0, self)  # index 0 is the locations of FIRST object in array

    def isFull(self):
        return self.BagSize == self.ARSize

    def isEmpty(self):
        return self.BagSize == 0

    def size(self):
        return self.BagSize

    def put(self,o):
        if not self.isFull():
            self.Array[self.BagSize] = o
            self.BagSize = self.BagSize + 1
        else:
            raise RuntimeError("bag full")

    def get(self, index):
        if not self.isEmpty():
            self.Array[index] = self.Array[self.BagSize-1]
            self.BagSize = self.BagSize - 1
            return self.Array[index]
        else:
            raise RuntimeError("bag empty, nothing to return")
            
def main():
    b = Bag()
    b.put(10)
    b.put(20)
    b.put(30)
    b.put(40)
    b.put(50)
    b.put(60)
    b.put(70)
    b.put(80)
    b.put(90)
    for d in b:
        print(d)
    print()

    print(b.get(3))
    print(b.get(5))
    print(b.get(0))
    print()
    for d in b:
        print(d)
    print()

main()
