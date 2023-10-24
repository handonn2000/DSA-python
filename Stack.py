class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.storage = []
    def __str__(self):
        return str(self.storage)

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is full!")
        
        self.storage.append(value)
        self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack already empty!")
        self.storage.pop()
        self.top -= 1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top >= self.capacity - 1
    
stack = Stack(3)
print(stack.isEmpty())

stack.push(5)
stack.push(10)
print(stack)

stack.pop()
print(stack)

stack.push(15)
stack.push(20)
print(stack.isFull())


    