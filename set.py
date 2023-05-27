new_set = {1, 2, 3, 4, 5, 6, 7}
print(new_set)

set2 = {5, 6, 7, 8, 9, 10, 11}
print(set2)

new_set.add(0)
print(new_set)

set3 = new_set.intersection(set2)
print(set3)

set4 = new_set.difference(set2)
print(set4)

set5 = new_set.symmetric_difference(set2)
print(set5)
