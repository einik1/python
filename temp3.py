# -*- coding: utf-8 -*-

import animal


def main():
   dog = animal.Dog()
   print(dog.__str__())
   dog2 = animal.Dog("kini", 100)
   print(dog2.__str__())
   dog2.setName("keito")
   dog2.birthday()
   print(dog2.__str__())

if __name__ == '__main__':
    main()