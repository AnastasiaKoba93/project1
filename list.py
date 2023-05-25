list =[1,2,3]
list_1 = ['Nastya','Koba',30]
list_2 = ['name','surname','age']
print(list,list_1,list_2)

list_1 [1] = 'city'
print(list,list_1,list_2)

dictionary_ ={
    'month': 'may',
    'city' : 'Kharkiv'
}
new_list = list_1
print(new_list)

new_list .append(dictionary_)
print('new_list with {} '.format(new_list))

dictionary_ .update({'new_list': list })
print('dictionary with list {}'.format(dictionary_))