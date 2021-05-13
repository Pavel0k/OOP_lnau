class one:
    def __init__(self):
        self.n = 10
    def total(self, a):
        return self.n+int(a)
class two(one):
    def __init__(self):
        self.s ="Hi!!!"
    def total(self, a):
        return len(self.s+str(a))
o1=one()
o2=two()
print(o1.total(3))
print(o1.total(45))