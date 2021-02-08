# 4. Set Methods and Set Math
new_set = set([1, 2, 4])

new_set.add(5)
print(new_set)

new_set.add('Alessandro')
print(new_set)
new_set.remove('Alessandro')
print(new_set)

new_set.discard('alessandro')  # removes without giving an error
print(new_set)

a = new_set.copy()
print('-----------')
print(a)
a.clear()
print(a)

print('-----------SET------------')
math_students = {"Jane", "Matthew", "Alessandro", "José"}
biology_students = {"Jane", "Matthew", "Alessandro"}

print(math_students.union(biology_students)) # Union will mix both sets without duplicating them
print(math_students.intersection(biology_students)) # Intersect will mix both sets with identical items
