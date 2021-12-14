class Pet():

    def __init__(self, name,age,color):
        self.name=name
        self.age=age
        self.color=color

    def sound(self):
        pass

    def show(self):
        print(self.name)

    def Type(self):
        print('Домашнее животное')

class Dog(Pet):

    def sound(self):
        print('GAF')

    def type(self):
        print('Dog')

class Cat(Pet):
    def sound(self):
        print('maaayy')
    def type(self):
        print('Cat')

class Perrot(Pet):
    def sound(self):
        print('asdasd')
    def type(self):
        print('Parriot')


Dolly= Dog('Dolly', 12, 'Red')
Murka=Cat('Murka', 10, 'Black')

Zoo= [Dolly, Murka]
for i in Zoo:
    i.show()
    i.sound()
    i.type()
    print('----')

