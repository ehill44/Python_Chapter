words= "It's thanksgiving day. It's my birthday, too!" #find and replace
print words.find('day', 0, len(words))
print words.replace('day', 'month')

list = [2, 54, -2, 7, 12, 98] #replace what is in parenthesis with appropriate list
print min(list), max(list)

list1=[x]    #first and last
print list1[0] , list1[len(list1)]

list1=['hello',1,2,3,4,5,'world'] 
print list1[0] , list1[len(list1)-1]


list2=[6,10,2,3,8,7];  #new list
list2.sort();
newlist=list2[0:len(list2)/2];
secondhalf=list2[len(list2)/2:len(list2)];
newlist.append(secondhalf) #need to determine how to push things to the beginning of the list, what we did here is technically correct, but brackets are misplaced
print newlist



