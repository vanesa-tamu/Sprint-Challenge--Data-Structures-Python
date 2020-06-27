class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.amount = 0

    def append(self, item):
        self.buffer[self.amount] = item
        self.amount +=1
        if self.amount == self.capacity:
            self.amount = 0

    def get(self):
        return [item for item in self.buffer if item != None]
