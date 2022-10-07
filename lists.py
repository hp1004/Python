#Create a list using []
a=[2, 4, 8 ]
#Print the list using print() Function 
print(a)

#Acess using index using a[0], a[1]
print(a[1])

#change the value of list using 
a[0]=98
print(a)

#we can create a list with items of different types
c=[1, 3, "Alex", 1.2]
print(c)

#List slicing 
friends =["alex", "Tom", "John", "sam", 69]
print(friends[0:3])
print(friends[-3:])

#List Methods 
l1 = [1,9,5,4,3]
print(l1)
l1.sort() #sorts the list
print(l1)
l1.reverse() #reverse the list
print(l1)
l1.append(45) #adds 45 at the end of list
print(l1)
l1.insert(0,544) #inseets 54 at index 0
print(l1)
l1.pop(2) #removes element at index2
print(l1)
l1.remove(4) #removes  from the list
print(l1)
l1.insert(2,54) #inseets 54 at index 0
print(l1)