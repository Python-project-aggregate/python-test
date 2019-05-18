import random
# class RandomGen:
#     def __init__(self,start = 1, stop = 100, count = 10):
#         self.start = start
#         self.stop = stop
#         self.count = count
#
#     def generate(self):
#         return [random.randint(self.start, self.stop) for i in range(self.count)]
# print(RandomGen().generate())
class RandomGen:
    @classmethod
    def generate(cls, start = 1, stop = 100, count =10):
        return [random.randint(start, stop) for i in range(count)]

print(RandomGen().generate())
