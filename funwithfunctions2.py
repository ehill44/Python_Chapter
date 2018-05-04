def multiply(lists,number):
    for i in range(len(lists)):
        lists[i]*=number
    return lists
a=[5,8,11,22]
b= multiply(a,5)
print b