# -*- coding: utf-8 -*-
import types
class BigThing:
    def __init__(self,var = None):
        self.__thing = var

    def size(self):
        if type(self.__thing) is int:
            return self.__thing
        return len(self.__thing)

    def getThing(self):
        return self.__thing


class BigCat(BigThing):
    def __init__(self,var, name = ""):
        BigThing.__init__(self, var)
        self.__name = name

    def size(self):
        if 15< self.getThing() < 20:
            return "Fat"
        if self.getThing() > 20:
            return "Very Fat"
        else:
            return "OK"


def main():
    thing = BigThing("table")
    print(thing.size())
    latif = BigCat(22, "Latif")
    one = BigCat(1, "1")
    two = BigCat(16, "2")
    print latif.size()
    print one.size()
    print two.size()

if __name__ == '__main__':
    main()