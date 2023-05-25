import copy

dictionary = {}

new_dict = {
    'name': 'Nastya' ,
    'surname': 'Koba' ,
    'age' : 30
}
print(new_dict)

update_dictionary = {
    'gender': 'women'
}

new_dict.update(update_dictionary)
print(new_dict)

new_dict.pop('gender')
print(new_dict)

popped_item = new_dict.pop('age')
print('popped_item {}'.format(popped_item))
print(new_dict)

link_copied_dict = new_dict
deep_copy = copy.deepcopy(new_dict)
print(id(deep_copy))

new_dict['nested_dict'] = update_dictionary
print(new_dict)

new_dict['city'] = {
    'name': 'Nastya' ,
    'surname': 'Koba' ,
    'age' : 30
}
print(new_dict)

list_of_keys = new_dict.keys()
print(list_of_keys)

list_of_values = new_dict.values()
print(list_of_values)

