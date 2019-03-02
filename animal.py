# -*- coding: utf-8 -*-

class Dog:
    def __init__(self, name="amado", age=6):
        self.__name = name
        self.__age = age

    def birthday(self):
        self.__age += 1

    def getAge(self):
        return self.__age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def __str__(self):
        return "name: {}, age: {}".format(self.getName(), self.getAge())


def main():
  print("this main will not run in case of import")


if __name__ == '__main__':
    main()