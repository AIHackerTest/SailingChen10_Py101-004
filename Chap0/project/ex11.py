# coding=utf-8

print ("How old are you?"),
age = input()  # raw_input used in python2, but input in python3
print ("How tall are you?"),
height = input()
print ("How much do you weigh?"),
weight = input()

print ("So, you're %r old, %r tall and %r heavy." % (age, height, weight))
