numbers = dict(first=1, second=2, third=3)

squared_numbers = {key: value ** 2 for key, value in numbers.items()}

print(squared_numbers)

names = dict(name1="alessandro", name2="lili", name3="biscoito")

capitalize = {n: v.capitalize() for n, v in names.items()}
print(capitalize)

number_list = list(range(0, 1000))


print({num: ("ímpar" if num % 2 == 1 else "par") for num in number_list})
