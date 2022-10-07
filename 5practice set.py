# Q1- Write a program to store seven colours in a list enter by a user

f1 = input("Enter Color Number 1: ")
f2 = input("Enter Color Number 2: ")
f3 = input("Enter Color Number 3: ")
f4 = input("Enter Color Number 4: ")
f5 = input("Enter Color Number 5: ")
f6 = input("Enter Color Number 6: ")
f7 = input("Enter Color Number 7: ")

myColorList = [f1, f2, f3, f4, f5, f6, f7]
print(myColorList)

# Q2 Write a program toaccept marks of 6 students and display them in a sorted forms
 

m1 = int(input("Enter Marks for Student Number 1: "))
m2 = int(input("Enter Marks for Student Number 2: "))
m3 = int(input("Enter Marks for Student Number 3: "))
m4 = int(input("Enter Marks for Student Number 4: "))
m5 = int(input("Enter Marks for Student Number 5: "))
m6 = int(input("Enter Marks for Student Number 6: "))

myMarkList =[m1, m2, m3, m4, m5, m6]
myMarkList.sort()
print(myMarkList)

# Q-check that a tupple cannot be changed in a python

a=(2, 4, 6, 8)
a[0]=3
print(a)

# Q-Write a program to sum a list with 4 numbers

a = [2, 4, 6, 8]
print(a[0] + a[1] +a[3]+a[4]+a[2])
print(sum(a))

#write a program to count the number of zeros in the following table
t=(7,0,8,0,0,9)
print(t.count(0))