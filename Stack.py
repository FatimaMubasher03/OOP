class Stack:
	def __init__(self, size=100):
		self._arraySize = size
		self._array = [None]*size
		self._top = 0

	def size(self):
		return self._top

	def isEmpty(self):
		return self.size() == 0 #   or   self._top == 0

	def isFull(self):
		return self.size() == self._arraySize    #    or return self._top == self._arraySize

	def push(self, val):
		if not self.isFull():
			self._array[self._top] = val
			self._top = (self._top + 1)
		else:
			raise RuntimeError("stack full")

	def peek(self):
		if not self.isEmpty():
			return self._array[self._top-1]
		else:
			raise RuntimeError("stack empty, nothing to return")

	def pop(self):
		val = self.peek()
		self._top = self._top - 1
		return val

def main():
    s = Stack()
    print(s.isEmpty())
    print(s.size())
    s.push(20)
    print(s.size())
    s.push(50)
    print(s.size())
    s.push(10)
    print(s.size())
    s.push(90)
    print(s.size())
    print(s.isEmpty())
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push(50)
    s.push(10)
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())    # comment this line
    print(s.isEmpty())

main()