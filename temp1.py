# -*- coding: utf-8 -*-

import sys
import os
import urllib

def abba():
    sant = raw_input("enter your sentence here:\n")
    sant = sant.replace("a","aba")
    sant = sant.replace("e","ebe")
    sant = sant.replace("i","ibi")
    sant = sant.replace("o","obo")
    sant = sant.replace("u","ubu")

def fiveDigits(s):
    return len(s) == 5

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def num():
        con = True
        while con:
            sant = raw_input("enter your number here:\n")
            con = (not fiveDigits(sant)) or (not is_number(sant))

        print sant
        a=0
        for i in sant:
            if a<4:
                print "{}, ".format(i),
                a+=1
            else:
                print i

        print ord(sant[0])+ord(sant[1])+ord(sant[2])+ord(sant[3])+ord(sant[4])-240

def mult(a,b):
    return a*b

def div(a,b):
    if b!=0:
        return a/b
    return "illegal"

def copyMach():
    SOURCE = r'C:\Users\kobi\Desktop\project\fire.txt'
    DEST = r'C:\Users\kobi\Desktop\project\empty.txt'
    with open(SOURCE, 'r') as inpote_file:
        with open(DEST, 'a') as outpote_file:
            for line in inpote_file:
                outpote_file.write(line)
    with open(DEST, 'r') as checkFile:
        for line in checkFile:
            print line,

def doHomework(line):
    i = 0
    while line[i] != " ":
        i += 1
    a = float(line[:i])
    opr = line[i+1]
    b = float(line[i+2:])

    if opr == "+":
        return a+b
    elif opr == "-":
        return a-b
    elif opr == "*":
        return a*b
    elif opr == "/":
        return a/b
    else:
        raise ValueError('illegal opr')

def doHomeworkAcceptArgsFromPycharm():
    try:
        homework = open(sys.argv[1], 'r')
    except:
        print "nosuchfile"
        return

    try:
        sol = open(sys.argv[2], 'a')
    except:
        print "nosuchfile"
        homework.close()

    for line in homework:
        try:
            sol.write(str(doHomework(line))+"\n")
        except Exception, e:
            sol.write(str(e) + "\n")

    homework.close()
    sol.close()

def main():
    sys


if __name__ == '__main__':
    main()