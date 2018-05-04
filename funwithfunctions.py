def odd_even():
    for num in range(20):
        
        if (num%2==0):
            print "Number is {}. This is an even number.".format(num)
        else:
            print "Number is {}. This is an odd number.".format(num)
    return range(20) #make sure the return statement is inline with for, otherwise it only runs the loop once
print odd_even()

def multiply(lists,number):
    for i in range(len(lists)):
        lists[i]*=number
    return lists
a=[5,8,11,22]
b= multiply(a,5)
print b

def layeredfunction(listz):
    newlist=[]
    for i in range(len(listz)):
        listz[i]=1
        newlist= newlist.append(listz[i])
    return newlist
    a=[1,3,4]
    x= layeredfunction(multiples([a,2))
    print x

