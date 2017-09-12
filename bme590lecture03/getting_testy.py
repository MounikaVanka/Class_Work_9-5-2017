# import pytest


def add(a, b):
    if ((type(a) != int and type(a) != float) or
       (type(b) != int and type(b) != float)):
        print("INVALID INPUT")
        return "invalid"
    elif(a < 0 or b < 0):
        print(0)
        return 0
    else:
        c = a + b
        print(c)
        return c


# a = int(input("enter 1st Number "))
# b = int(input("Enter 2nd Number "))

# add(a, b)

def testOne():
    assert(add(-2, 1) == 0)


def testTwo():
    assert(add(1, 1) == 2)


def testThree():
    assert(add(1, 1) == 2)


def testFour():
    assert(add(3.1, 4.3) == 7.4)


def testFive():
    assert(add(3.1, 1) == 4.1)


def testSix():
    assert(add("3.1", 1) == "invalid")


testOne()
testTwo()
testThree()
testFour()
testFive()
testSix()
