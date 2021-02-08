nums = list(range(0, 101))

print([x * 2 for x in nums])
print([(x / 2) + 0.5 for x in nums])

print(type([str(x) for x in nums]))
print('-------------------')
print([x for x in nums if x % 2 == 0])
print([x for x in nums if x % 2 != 0])
print([x * 2 if x % 2 == 0 else x / 2 for x in nums])
print('-------------------')
with_vowels = "This is so much fun!"
with_vowels = ''.join(char for char in with_vowels if char not in "aeiou")
print(with_vowels)
print('-------------------')
print('-------------------')
with_numbers = "I've got 1 million dollars!"
with_numbers = ''.join(int for int in with_numbers if int not in "1234")
print(with_numbers)
print('-------------------')
name = 'alessandro'
print(name.upper())
print(name.capitalize())
print(name.lower())

print(name.islower())
print(name.isupper())
print('-------------------')
print('-------------------')
nested_list = [[1, 2, 3], [4, 5, 6]]
print(nested_list[0][0])
print(nested_list[0][1])
print(nested_list[0][2])
print(nested_list[0])
print(nested_list[0][-1])
print('-------------------')
for l in nested_list:
    for val in l:
        print(val)

print('-------------------')
print('-------------------')
coords = [[10.423, 9.132], [37.212, 64.333]]
for c in coords:
    for val in c:
        print(val)
print('-------------------')
(print(val) for val in l for l in coords)

# 12. Nested Lists
