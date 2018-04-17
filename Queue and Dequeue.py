#Ellene Gay S. Daniel
#Queue and Dequeue


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(5)
q.enqueue(20)
q.enqueue(40)
q.enqueue(50)
q.enqueue(80)
q.enqueue(100)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
