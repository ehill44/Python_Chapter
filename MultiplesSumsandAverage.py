def function1():
for i in range(1,10,2):
    print i

# both of these functions will produce the same result
for i in range(1,11):
   if i%2==0:
    continue;
   print i

return i 
#part 2

for i in range(5,101):
    if i %5==0:
        print i


#summing lists

a=[1,2,5,10,255,3]
print sum(a)

#average lists

a=[1,2,5,10,255,3]
average= sum(a)/len(a)
print average