class stack:
    def __init__(self):
        self.items = []

    def push(self, item: object):
        self.items.append(item)
    def pop(self):
         print("pop an item")
         return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
       return len(self.items)
