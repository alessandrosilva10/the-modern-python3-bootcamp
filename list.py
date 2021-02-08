# watch 11. List Methods Append, Insert, and Extend

lista = []
lista.append(1)
lista.append(2)
lista.append(3)
lista2 = [4, 5, 6]
lista.extend(lista2)
lista.insert(0, 10)
lista.insert(len(lista), 11)
lista2.clear()
lista.pop(0)  # index
last_item = lista.pop()  # remove last item by default
print(lista)
print(last_item)
print(lista2)

fruits = ["Orange", "Lemon", "Apple", "Orange", "Lemon", "Apple"]
fruits.remove("Lemon")
print(fruits)
print(fruits.index("Apple"))
print(fruits.index("Apple", 1, -1))
print(fruits.count("Apple"))
fruits.reverse()
print(fruits)
' '.join(fruits)
print('.'.join(fruits))
print("------")
tasks = ["a", "c", "d", "b"]
tasks.sort()
print(tasks)
print(len(tasks))
tasks = list(range(0, 10))
print(tasks)
print(len(tasks))
print(type(tasks))
print(tasks[2])
print(tasks[-1])
print(tasks[-2])
print(9 in tasks)  # True
print(10 in tasks)  # False

# Slice
print(fruits)
print(fruits[:2])
print(fruits[:-2])
print(fruits[-2:])
print(fruits[2:4])
print(fruits[0::2])
print(fruits[::-1]) # reverse
print(fruits[0][::-1]) # reverse
print("-------------")
numbers = [0, 1]
print(numbers)
numbers[1], numbers[0] = numbers[0], numbers[1]
print(numbers)
"""
a = [1, 2, 3, 5, 6]

#for i in range(1, 10, 1000):
        #print(i)

r = range(1, 10, 2)
for a in r:
        print(a)

#for i in (7, 0, -1):
        #print(i)

#for c in "coffee":
        #print(100*c)"""
