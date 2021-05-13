class videokard:
    def __init__(self, name, model, value):
        self.name = name
        self.model = model
        self.value = value
        self.cod = name +"" 'GV-N3098' + '-MV1'


    def fullinfo(self):
        return '{} {}'. format(self.name, self.model)


vid_1 = videokard ('ASUS', 'RTX-3090', 124000)
vid_2 = videokard ('GIGABYTE', "RTX-3080TI", 86000)

vid_1.fullinfo()

print(videokard.fullinfo(vid_1))
print(videokard.fullinfo(vid_2))
print(vid_1.cod)





