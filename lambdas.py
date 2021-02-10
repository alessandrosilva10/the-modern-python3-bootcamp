def square(num): return num * num


add = lambda a, b: a + b
square2 = lambda num: num * num

print(square(3))
print(square2(4))
print(square.__name__)
print(square2.__name__)
print(add(2, 4))
