# Immutable and ordered

new_tuple = (1, 4, 2, 3)
print(new_tuple)
print(new_tuple[1]) # 4
print(new_tuple[-1]) # 3

# Tuples can be used as keys in dictionaries:
locations = {
    (35.6895, 39.6917): 'Assis',
    (15.1835, 29.2412): 'Marília',
}


for n in new_tuple:
    print(n)

print(len(new_tuple)-1)
print(locations[(35.6895, 39.6917)])

print(new_tuple[2::3])

