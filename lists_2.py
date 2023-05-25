import copy

list = [1,2,3,[0,1,2],5]
print('list id {}'.format(id(list)))
print('list {}'.format(list))

new_list = list
print('new list {}'.format(id(new_list)))
print('new list {}'.format(new_list))

copy_list = new_list
print('copy_list {}' .format(id(copy_list)))
print('copy list {}'.format(copy_list))

copy_list .append(6)

#Shallow copy
shallow_copy_new_list = copy.copy(new_list)
print('shallow copy new list id {}' .format(id(shallow_copy_new_list)))
print('shallow copy new list {}' .format(shallow_copy_new_list))

#Depp copy
deep_copy_new_list = copy. deepcopy(new_list)
print('deep copy new list id {}'. format(id(deep_copy_new_list)))
print('depp copy {}'.format(deep_copy_new_list))


list[3] .append(7)
print('list id {}'.format(id(list)))
print('list {}'.format(list))
print('new list {}'.format(id(new_list)))
print('new list {}'.format(new_list))
print('copy_list {}' .format(id(copy_list)))
print('copy list {}'.format(copy_list))
print('shallow copy new list id {}' .format(id(shallow_copy_new_list)))
print('shallow copy new list {}' .format(shallow_copy_new_list))
print('deep copy new list id {}'. format(id(deep_copy_new_list)))
print('depp copy {}'.format(deep_copy_new_list))














