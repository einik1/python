# -*- coding: utf-8 -*-

def calc():
    total = 0
    for i in shoping_cart:
        if i in prices:
            total += shoping_cart[i]*prices[i]
        else:
            print "no price for {}, calc is without {}".format(i, i)
    return total

prices = {"banana": 10, "apples": 8, "bread": 7, "chease": 20, "juice": 15}
shoping_cart = {"banana": 2, "bread": 3, "chease": 1}

print calc()

shoping_cart["grapes"] = 50

print calc()


def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code


if __name__ == '__main__':
    main()