class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.front = -1
        self.rear = -1

    def display(self):
        print("[front, rear] = [{0}, {1}]".format(self.front, self.rear))
        print(self.queue)

    def isFull(self):
        return len(self.queue) >= self.size
    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        if self.isFull():
            raise Exception("Queue is full")

        if not self.isEmpty() and self.front > 0:
            self.front -= 1
        else:
            self.front = 0

        
        if self.rear < self.size - 1:
            self.rear += 1
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front += 1
        return self.queue.pop(0)
    
myQueue = Queue(5)
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)

myQueue.display()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
# myQueue.dequeue()
myQueue.display()
myQueue.enqueue(6)
myQueue.display()
myQueue.enqueue(7)
myQueue.display()
myQueue.dequeue()
myQueue.display()
# myQueue.enqueue(8)
# myQueue.display()
# myQueue.enqueue(9)
# myQueue.display()