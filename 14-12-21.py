class Employer(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + str(self.age)

    def printof(self):
        print('')

class President(Employer):
    def printof(self):
        print(f'"ПРЕЗИДЕНТ",Имя его {self.name}, возраст {self.age}')

class Manager(Employer):
    def printof(self):
        print(f'МЕНЕДЖЕР, Имя его {self.name}, возраст {self.age}')

Obama=President('Черный пацан',70)
Petr=Manager('Просто Петя', 35)

All=[Obama,Petr]

for i in All:
    i.printof()

print(Obama)