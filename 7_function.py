#!/usr/bin/env python3
# Python3
'''

'''


def guess(x):
    if x == 0:
        return 0
    else:
        return 'a'


def myFirstFunction():
    print('Hello world!')


def mySecondFunction(name):
    print('Your name is %s' % name)


def myThridFunction(name,age):
    print('name = %s, age = %d' % (name, age))


def myFourthFunction(name, age, **others):
    print('Fourth: name = %s, age = %d, others = %s' % (name, age, others))


def myFifthFunction(name, age, *descriptions, **others):
    print('Fifth: name = %s, age = %d, descriptions = %s, others = %s' % (name, age, descriptions, others))


def mySixthFunction(name, age, *descriptions, command = 'Win', **others):
    print('Sixth: name = %s, age = %d, descriptions = %s, others = %s, command = %s' % (name, age, descriptions, others, command))


if __name__ == '__main__':
    myFirstFunction()
    mySecondFunction('BalterNotz')
    mySecondFunction(name='BalterNotz')
    myThridFunction(name='BalterNotz', age=27)
    myThridFunction(age = 27, name = 'BalterNotz')
    myFourthFunction('BalterNotz', 27, job='IT')
    myFourthFunction('BalterNotz', 27, **{'job':'IT'})
    myFourthFunction(name='BalterNotz', age = 27, job = 'IT', address = 'Henan')
    myFourthFunction('BalterNotz',  27, job = 'IT', address = 'Henan')
    myFifthFunction('BalterNotz', 27, 'man', 'good', 'honest', job = 'IT', address = 'Henan')
    mySixthFunction('BalterNotz', 27, 'man', 'good', 'honest', job = 'IT', address = 'Henan')
    print(guess(0))
    print(guess(1))


