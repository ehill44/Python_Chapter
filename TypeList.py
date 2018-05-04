list1=[5,7,"please",9,"stop"]
sums=0
string=''
for i in list1:
    if isinstance(i, int):
        sums+=i
    if isinstance(i,str):
        string.append(i)
integers=0
stringz=0
    if isinstance(i,int):
        integers=integers+1
        types= 'number'
    if isinstance(i,str):
        stringz=stringz+1
        types='string'
    if integer>0 and stringz>0:
    print "The list you entered is of mixed type"

print "String:"+string
print "Sum:"+sums
print "The list you entered is of" , types ,"type""




 #     list1=[5,7,"please",9,"stop"]
# for i in range(0,len(list1)-1):
#     if isinstance(list1, int):
#        sum+=sum(list1);
#        print sum
       

#     if type(list1[i]) == int:
#         sum+=sum(list[i])
#         print sum
    

#  if list1[i] type=str:
#     list1[i]+=

#     list=["please", help"]
#     print 

# print "The list you entered is of" , type ,"type"
# print "String:" , 
# print "Sum:" , sum