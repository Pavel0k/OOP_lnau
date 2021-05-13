class videokard:
    num_of_emps=0
    raise_amount = 1.07
    def __init__(self, name, model, value):
        self.name = name
        self.model = model
        self.value = value
        self.cod = name +"" 'GV-N3098' + '-MV1'
        videokard.num_of_emps+= 2

    def fullinfo(self):
        return '{} {}'. format(self.name, self.model)

    def apply_raise(self):
        self.value = int(self.value * self.raise_amount)
vid_1 = videokard ('ASUS', 'RTX-3090', 124000)
vid_2 = videokard ('GIGABYTE', "RTX-3080TI", 86000)

print(videokard.num_of_emps)
print(videokard.fullinfo(vid_1))
print(vid_1.value)
vid_1.apply_raise()
print(vid_1.value)
print(videokard.fullinfo(vid_2))
print(vid_2.value)
vid_2.apply_raise()
print(vid_2.va)