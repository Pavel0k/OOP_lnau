class one:
    def __init__(self,value):
        self.__var = value

    @property
    def VA(self):
        return self.__var

    @VA.setter
    def VA(self, value):
        self.__var = value

    @VA.deleter
    def VA(self):
        del self.__var
o=one(5)
o.VA=30
print(o.VA)
del o.VA





