import random
class RandomGen:
    def __init__(self, start = 1, stop = 100, count = 10):
        self.start = start
        self.stop = stop
        self.count = count
        self._gen = self._generate()
    def _generate(self):
        while True:
            yield random.randint(self.start , self.stop)

    def generate(self):
        return [next(self._gen) for i in range(self.count)]

print(RandomGen().generate())