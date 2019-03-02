import random
CTL = (4, 4)
class CrazyPlane:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def update_position(self):
        self.__x += random.randint(-1,1)
        self.__y += random.randint(-1,1)

    def get_position(self):
        return self.__x, self.__y

    def set_position(self, x, y):
        if (x,y) == CTL:
            print "tower loc"
        elif x < 0 or y < 0:
            print "illegal loc"
        else:
            self.__x = x
            self.y = y
            print "Loc Chanched"
    def __str__(self):
        return " plane pos: {}".format(self.get_position())


class NormalPlane:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def update_position(self):
        self.__x += 1
        self.__y += 1

    def get_position(self):
        return self.__x, self.__y

def main():
    print "this main is nit reached if this file is imported"

if __name__ == '__main__':
    main()