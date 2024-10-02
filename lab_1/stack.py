class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def isFull(self):
        return False

    def isEmpty(self):
        return self.empty()