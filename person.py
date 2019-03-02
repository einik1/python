# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name="mike", age=28):
        self.__name = name
        self.__age= age

    def say(self):
        print "hey"

    def __str__(self):
        return 'person {} is {} yo'.format(self.getName(), self.getAge())

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age= age

class Teacher(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name,age)
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def say(self):
        print 'Good morning students!!'

    def __str__(self):
        return "Teacher {} is {} yo and makes {} dollars".format(self.getName(), self.getAge(),self.__salary)


class Student(Person):
    def __init__(self, name = "kobi", age=29, grade=100):
        super(Student, self).__init__(name, age)
        self.__grade = grade

    def getGrade(self):
        return self.__grade

    def setGrade(self, grade):
        self.__grade = grade

class CyberStudent(Student):

    def __init__(self, name, age,grade,cybergrade):
        super(Student,self).__init__(name,age,grade)
        self.__CyberGrade = cybergrade


def main():
    None

if __name__ == '__main__':
    main()