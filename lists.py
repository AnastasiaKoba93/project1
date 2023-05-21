list = [1,2,3]
print(list)

new_list = list .copy()
new_list .append(7)

print(new_list)
print(list)

new_list .insert(7 ,10)
print(new_list)

list .extend(new_list)
print(new_list)

new_list .pop(1)
print(new_list)

print(list .index(3))
print(list .remove(1))

print(new_list[0])
new_list[0] = 8
print(new_list)

subset_list = [1,2,3,4,5,6,7,8,9]
print(subset_list)

subset_list_1 = subset_list[::-1]
print(subset_list_1)

subset_list_3 =subset_list[1:7:2]
print(subset_list_3)

subset_list_4 = subset_list[2:6]
print(subset_list_4)

