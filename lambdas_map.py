nums = [1, 2, 3, 4, 5, 6]

doubles = map(lambda x: x * 2, nums)

print(list(doubles))

for d in doubles:
    print(d)

people = ["Darcy", "Christina", "Alessandro"]

peeps = map(lambda name: name.upper(), people)

print(list(peeps))


def double(x): return x * 3


d = map(double, nums)
print(list(d))
