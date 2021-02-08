first_dic = {
    "name": "Alessandro",
    "age": 29
}

new = dict(name="Alessandro", age=29)

dicts = [{'a': 1, 'b': 2, 'c': 3},
         {'a': 1, 'd': 2, 'c': 'foo'},
         {'a': 57, 'c': 3}]

print(dicts[0]["a"])
print(dicts[2]["a"])
print("My age is: " + str(new["age"]))

try:
    print(new["cat1"])
except KeyError as e:
    print(e)
print("-----------")
for n in new.values():
    print(n)

for n in new.keys():
    print(n)

for key, value in new.items():
    print(value)
print("-----------")
print("-----------")
print("name" in new)  # Returns true
print("nam1e" in new)  # Returns false
print(29 in new.values())  # Returns true
print(27 in new.values())  # Returns false
print("-----------")
print("-----------")
print("aaaaaaaaaaaaaa")
a = new.copy()
print(a)
new.clear() # clear the whole dict
print(new)
print(a is new)
print("-----------")
print("-----------")
b = {}.fromkeys(["name", "age", "address", "email"], "unknow")
b.fromkeys('phone', '18997029578')
c = {}.fromkeys(range(0,11), 'null')
print(b)
print(c)

# get
print(c.get(1))
print(b.get('name'))

# pop
b.pop('name')
print(b)

# popitem remove a random key
b.popitem()
print(b)

dd = dict(a=1, b=2, c=3)
ee = dict(d=4)
ee.update(dd)
print(ee)