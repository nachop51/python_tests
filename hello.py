# message = 'This is a message'
# print('Hello')
# print("A lot of other things %s %d" %(message, 10))

# i = 0
# while i < 10:
#   print(i)
#   i += 1
# print("This is outside the loop")
# for x in range(10):
#   i = 0
#   print("Indentation is crucial")
#   while i < 10:
#     print("Nested loop nigga")
#     i += 1
# xd = "still testing python, look"
# print(xd)
# item = 0
# for item in range(10):
#     if item == 5:
#         print("Item is %d" % (item))
# print(item)
# item += 1
# if item == 10:
#     print("Item ended his iteration")
# a = len(xd)
# print(a)
# i = 0
# while i < a:
#     print(xd[i])
#     i += 1
# for element in xd:
#     print(element, end='')
# print('\n')
# for element in range(0, len(xd)):
#     print(xd[element], end='')
# print('\n')
# for i, v in enumerate(xd):
#     print(v, end='')
# print('\n')

import random
import math


def positive_or_negative():
    n = random.randint(-100, 100)
    # use n as your number
    if n < 0:
        print("n:%d is negative" % (n))
    if n > 0:
        print("n:%d is positive" % (n))
    if n == 0:
        print("n:%d is zero" % (n))


def last_digit():
    n = random.randint(-100, 100)
    lastDigit = math.fmod(n, -10)
    if (lastDigit > 5):
        print("Last digit of %d is %d and is greather than 5" % (n, lastDigit))
    elif (lastDigit == 0):
        print("Last digit of %d is %d" % (n, lastDigit))
    else:
        print("Last digit of %d is %d and is less than 6 and not 0" %
              (n, lastDigit))


def while_numbers():
    char = 48
    while char <= 57:
        print("%c" % (char), end='')
        char += 1
    print()


def for_numbers():
    char = 48
    for char in range(char, 58):
        print("%c" % (char), end='')
        char += 1
    print()


def while_alphabets():
    char = 65
    while char <= 90:
        print("%c" % (char), end='')
        char += 1
    print()
    char = 97
    while char <= 122:
        print("%c" % (char), end='')
        char += 1
    print()

# trying both solutions just to practice the usage of the loops


def for_alphabets():
    char = 65
    for char in range(char, 91):
        print("%c" % (char), end='')
        char += 1
    print()
    char = 97
    for char in range(char, 122):
        print("%c" % (char), end='')
        char += 1
    print()


def for_triangle(size):
    if size > 0:
        for i in range(0, size):
            n = i
            for n in range(n, size - 1):
                print(".", end='')
                n += 1
            x = i + 1
            for x in range(0, x):
                print("#", end='')
                x -= 1
            print()
    else:
        print()

# trying both solutions just to practice the usage of the loops


def while_triangle(size):
    if size > 0:
        i = 0
        while i < size:
            n = i
            while n < size - 1:
                print(".", end='')
                n += 1
            x = i + 1
            while x > 0:
                print("#", end='')
                x -= 1
            print()
            i += 1
    else:
        print()


def print_test(char, number, s):
    print("Print with a new line")
    print("Print with no new line at the end", end='')
    print(" no new lineeeeeeee")
    print("Fomating things, look:\nChar:%c, Number:%d, String:'%s'" % (char, number, s), end ='')

def simple_function():
    print("Hello world!")

print("\n-----------------")
print("lets test the alphabets")
print("-----------------\n")

print("for\n")
for_alphabets()
print("\nwhile\n")
while_alphabets()

print("\n-----------------")
print("numbers?")
print("-----------------\n")

for_numbers()
while_numbers()

print("\n-----------------")
print("for tests for trianlge function")
print("-----------------\n")

for_triangle(1)
for_triangle(2)
for_triangle(5)
for_triangle(10)
# for_triangle(98)
# for_triangle(0)
# print("this should only print a new line up here")
# border case, remove the # to use

print("\n-----------------")
print("while tests for triangle function")
print("-----------------\n")

while_triangle(1)
while_triangle(2)
while_triangle(5)
while_triangle(10)
# while_triangle(98)
# while_triangle(0)
# print("this should only print a new line up here")
# border cases, remove the # to use

print("\n-----------------")
print("positive or negative test")
print("-----------------\n")

positive_or_negative()
positive_or_negative()
positive_or_negative()
positive_or_negative()

print("\n-----------------")
print("last digit test")
print("-----------------\n")

last_digit()
last_digit()
last_digit()
last_digit()

print("\n-----------------")
print("print usage test")
print("-----------------\n")

s = "This is a string\n"
print_test(s[10], 34, s)

print("\n-----------------")
print("simple function call")
print("-----------------\n")

simple_function()