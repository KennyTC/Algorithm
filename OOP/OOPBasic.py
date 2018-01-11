class Animal:
    def __init__(self, sex=None):
        self.sex = sex
    def getInfor(self):
        print("Sex:{}".format(self.sex))

class Dog(Animal):
    def __init__(self, sex=None, color=None):
        super(Dog, self).__init__(sex)
        self.haircolor = color

    def getInfor(self):
        super(Dog, self).getInfor()
        print("Hair color:{}".format(self.haircolor))

a = Animal("Male")
print(a.getInfor())
b = Dog("Male","Yellow")
print(b.getInfor())


