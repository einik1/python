# -*- coding: utf-8 -*-

def avg_diff(list1, list2):
    return float(sum([(list1[i]-list2[i]) for i in range(0, len(list1))]))/len(list1)

f = lambda x: x+2

g = lambda x: abs(x)

def doubleS(str):
    return "".join(map(lambda x: x+x, str))

def Sinon(x):
    return filter(lambda y: y % 3 == 0, range(1, x))

def Safrut(x):
    return reduce(lambda z, y: z + y, [int(str(x)[i]) for i in range(0, len(str(x)))])

def main():
    #print avg_diff([1, 2, 3, 4], [1, 1, 1, 1])
    #print f(-2)
    #list1 = [2, -8, 5, -6, -1, 3]
    #list1.sort(key=g)
    #print(list1)
    #string = 'kobi is the king'
    #print doubleS(string)
    #print Sinon(100)
    print [int(str(123)[i]) for i in range(0, len(str(123)))]
    print Safrut(123456789)


if __name__ == '__main__':
    main()