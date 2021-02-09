def print_colors(color):
    print(color)


def generate_numbers(first, second):
    numbers = range(first, second)
    for n in numbers:
        print(n)


print_colors("red")
print_colors("yellow")
print_colors("blue")

generate_numbers(0, 5)
generate_numbers(5, 10)
generate_numbers(10, 15)

# 6. Writing a coin_flip Function Using Random

from random import randrange


def flip_coin():
    if randrange(2) == 1:
        return "Heads"
    else:
        return "Tails"


print(flip_coin())


def show_information(name="Alessandro", lastname="Silva"):
    print(f'My name is {name} {lastname}')


show_information()


def add(a, b):
    return a + b


def math(a, b, fn=add):
    print(fn(a, b))


def subtract(a, b):
    return a - b


math(2, 1)
math(2, 1, subtract)


def exponent(num, pow):
    return num ** pow


print(exponent(pow=2, num=4))

name = "Alessandro"
print(name)


def global_name():
    global name
    name = "Silva"


global_name()
print(name)

# functions part II - 1. Introduction and args
