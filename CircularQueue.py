class CircularQueue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def display(self):
        print('[front, rear] = [{0},{1}]'.format(self.front, self.rear))
        print(self.queue)

    def isFull(self):
        if self.front == self.rear + 1:
            return True
        if len(self.queue) == self.size:
            return True
        return False

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is Full")

        if len(self.queue) == 0:
            self.front = 0
            self.rear = 0

        if self.rear == self.size:
            self.rear = 0
        else:
            self.rear += 1

        self.queue.insert(self.rear, value)

    def dequeue(self):
        if self.isEmpty():
            return

        self.queue.pop(self.front)
        if self.front == self.size:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1


obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
obj.display()

obj.dequeue()
obj.display()
obj.enqueue(6)
obj.display()
obj.dequeue()
obj.display()
obj.dequeue()
obj.display()
obj.enqueue(7)
obj.enqueue(8)
obj.display()
