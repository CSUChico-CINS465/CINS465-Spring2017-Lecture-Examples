#
# f = open("testfile1","w")
#
# f.write("Hello World")

f = open("testfile1","a")
a = [1,2,3,4]
for i in a:
    f.write(str(i)+"\n")


# f = open("testfile1","r")
#
# for line in f:
#     # print(line.strip())
#     print(int(line)+1)

class Person:

    def __init__(self,name,age=0):
        self.name=name
        self.age=age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

class Student(Person):

    def __init__(self,name,age=0,started=1900):
        Person.__init__(self,name,age)
        self.started=started

    def getAge(self):
        return self.age+4

    def getStarted(self):
        return self.started

person = Student("Victor",18,2016)
print(person.getName() + " is " + str(person.getAge())+ " started in " + str(person.getStarted()))
