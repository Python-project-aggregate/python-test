class Fib:
    def __init__(self):
        self. items = [0, 1, 1]
    def __iter__(self):
        return iter(self.items)
    def __len__(self):
        return len(self.items)
    def __call__(self, index):
        if index < 0:
            raise IndexError('Wrong Index')
        if index < len(self.items):
            return self.items[index]
        for i in range(len(self.items), index + 1):
            self.items.append(self.items[i-1] + self.items[i-2])
        return self.items[index]
print(Fib()(101))