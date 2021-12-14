class Diary(object):
    def __init__(self,path):
        self.path = path
        f=open(path, 'r', encoding='UTF-8')
        self.task=f.read().split('|')
        f.close()

    def get_tasks(self):
        return self.task

    def add_task(self,task):
        self.task.append(task)
        self.update_file()

    def update_file(self):
        r=open(self.path, 'w', encoding='UTF-8')
        r.write('|'.join(self.task))
        r.close()

    def delete_task_idex(self,index):
        self.index=index
        self.task.pop(index)
        self.update_file()

    def delete_task_name(self,name):
        self.task.remove(name)
        self.update_file()

Slovar=Diary('file.txt')
#string=input('Enter task:' )
#string2=input('Удалить индекс задания № ')
#Slovar.add_task(string)
#Slovar.delete_task_idex(int(string2))

string3=input('Удалить по имени ')
Slovar.delete_task_name(str(string3))