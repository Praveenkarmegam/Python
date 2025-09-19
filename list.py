# # list : It is represented by '[]' and it collects or store a set of values 
# # It can be strings, numbers, float, boolean, etc.. 

# # l1 = ['a','b','c']

# # l2 = [1,3,6.0,8j,10]

# # l3 = [True,False]

# # l4 = ['a','b','c',1,3,6.0,8j,10,True,False]

# # print(l1)
# # print(l2)
# # print(l3)
# # print(l4)
# # print(type(l1))
# # print(type(l2))


# # #range(e-1)

# # l1 = list(range(11))
# # print(l1)

# # #range(start,end-1)

# # l2 = list(range(5,11))
# # print(l2)


# # #range(start,end-1,step)

# # l3 = list(range(2,11,2))
# # print(l3)


# # l1 = list(range(7))
# # print(l1)

# # n = 3 
# # # n = -3 # multiplication can be done in negative values 

# # l2 = l1 * n
# # print(l2)


# l1 = [10,20,30,40,50,60,70]

# print(l1[2]) # 30
# print(l1[-4]) # 40
# print(l1[1:4]) # 20,30,40
# print(l1[:4]) # 10,20,30,40
# print(l1[1:]) # 20,30,40,50,60,70
# print(l1[::2]) # 10,30,50,70

# # l1[1:4] = ['A','B','C','D'] # values add with no limit 
# # print(l1)

# # # we can change the list - changeable

# # l1 = [10,20,30,40,50,60,70]
# # print(l1)

# # l1.append("orange") # direct adding the values
# # print(l1)

# # l1.insert(2,"Mango") # position 
# # print(l1)

# # # extend my list or collection

# # l2 = ['A','B','C','D'] 
# # l1.extend(l2)

# # print(l1)

# # # remove 
# # l1 = [10,20,30,40,50,60,70]

# # l1.remove(50)
# # print(l1)

# # # pop()
# # l1.pop()
# # l1.pop(0)

# # print(l1)

# # # delete
# # l1 = [10,20,30,40,50,60,70]

# # del l1[2:4]
# # print(l1)

# # #clear()

# # l1.clear()
# # print(l1)

# ## other methods 

# l1 = ['apple','banana','cherry','orange','cherry','APPLE','STRAWBERRY','PAPAYA','PINEAPPLE','GRAPES']
# # print(l1)

# # print(l1.index('cherry'))

# # print(l1.count('cherry'))

# # print(l1[::-1])

# # l1.reverse()
# # print(l1)

# # sort
# # l1.sort()
# # print(l1)

# # print(ord('A')) # a -97 but A - 67


# # # copy 
# # l1 = [1,2,3]

# # l2 = l1.copy()

# # # print(l1)
# # # print(l2)

# # l1.append(4)

# # print(l1)
# # print(l2)

# # l2.clear()

# # print(l1)
# # print(l2)


# # l1 = [10,20,30,40,50,-10]

# # print(max(l1))
# # print(min(l1))


# # nested lists:

# # l1 = [
# #     [1,2,3],[4,5,6],[7,8,9]
# # ]

# # print(l1)

# # l2 = [4,5,6]
# # l1.append(l2)
# # print(l1)


# # print(l1[1])
# # print(l1[1][2])

# # list comprehension - creating a new list from the existing collections 

# names = ['chinnu','thilipan','bhoomika','hema']

# names_with_a = []

# for item in names:
#     if 'n' in item:
#         print(item)
#         names_with_a.append(item)

# print(names_with_a)