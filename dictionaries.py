# # {key:value} - key: value pairs of items

# # ordered,changeable,allow duplicate values but not keys 

# d1 = {
#     'name':'chinnu',
#     'age':21,
#     'car':["bmw","vw"],
#     'married':False
# }

# # print(d1)
# # print(type(d1))
# # print(len(d1))
# # print(d1['name'])
# # print(d1.get('married')) # to get the values from the dictionary

# print(d1.keys())
# print(d1.values())
# print(d1.items())


# l1 = [('name', 'thilipan'), ('age', 20), ('bike', ['bmw', 'ns']), ('married',True)]

# d2 = dict(l1)
# print(d2)

# d3 = {'name': 'thilipan', 'age': 20, 'bike': ['bmw', 'ns'], 'married': True}

# d3['married'] = False
# print(d3)

# d3.update({'married':False})
# print(d3)

# d3.pop('married')
# print(d3)

# d3.popitem()
# print(d3)

# del d3['age']
# print(d3)

# d3.clear()
# print(d3)

# d1 = {'name': 'thilipan', 'age': 20, 'bike': ['bmw', 'ns'], 'married': True}


# for x in d1:
#     print(d1[x])
    

# for x in d1.items():
#     print(x)
    
# for key,value in d1.items():
#     print(f'{key=}and {value=}')
    
