class Queue:
    def __init__(self,size):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.size = size

    def isFull(self):
        return self.rear - self.front + 1 ==self.size

    def isEmpty(self):
        return self.rear < self.front

    def enqueue(self, item):
        if not self.isFull():
            self.queue.append(item)
            self.rear +=1
        else:
            print("queue is full")

    def dequeue(self):
        if not self.isEmpty():
            item = self.queue[self.front]
            self.front +=1
            return item
        else:
            print("queue is empty")
            return None

    def peek(self):
        if not self.isEmpty():
            return self.queue[self.front]
        else:
            return None
