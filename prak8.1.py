class one:
    def __init__(self, a, b):
        self.name = a
        self.sur = b

class two(one):
    def square(self):
        return self.name**self.sur

class three(two):
    def truck(self):
        return 'T:', self.name, " ", self.sur

o1 = three(3,4)

print(o1.truck())
print(o1.square())


