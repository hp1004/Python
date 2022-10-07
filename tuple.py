#creating a tuple using ()



t=(1, 2, 3, 4)
print(t)     
#you can't update tuple  
#t[0]=32
#print(t)

t1=() #empty tuple
t1=(1,)  #tuple with single element
t1=(1) #wrong way to declare a tuple with single element 
print(t1)

#printing the element of a tuple
print(t[0])

#tuples methods 
t=(1, 2, 3, 4, 1, 1, 1, 1)
print(t.count(1)) #return number of occurance of given value
print(t.index(2)) #return index of given input

#for more go and visit python.org
