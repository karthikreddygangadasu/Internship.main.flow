#LIST
mylist = [1,2,3,4,5,"Apple","Night"]

#1_Adding end of the list
mylist.append(6)

#2_ Adding at the particular position
mylist.insert(3,0)

#Modification of list
mylist[4]=7.2

#1_Removing using value
mylist.remove("Apple")

#2_Removing using index
mylist.pop(1)


print("Updated list:",mylist)

#SET

myset = {1,2,3,4,"a","b"}

#Adding
myset.add("c")

#Removing
myset.remove(3)

#Modification
myset.discard("a")
myset.add("z")

print("Updated set:",myset)


#DICTIONARY
mydict={'name': "Karthik",'Age':21,'city':"Guntur"}

#Adding
mydict.update({'Gender':"Male"})

#Removing
del mydict['city']

#modification
mydict['Age']=22

print("Updated Dictionary:",mydict)
