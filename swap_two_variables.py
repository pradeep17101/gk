#Name: T.Pradeep
#Lab:03
#Task:03
#Program:Swapping of two variables
#creating temp variable
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
temp=a
a=b
b=temp
print("After swapping")
print("a =",a)
print("b =",b)
#Swapping by tuple unpacking
a=input("Enter 'a'value:")
b=input("Enter 'b' value:")
a,b=b,a
print("After swapping by tuple unpacking i.e a,b=b,a")
print("a =",a)
print("b =",b)

#Output:
#Enter 'a'value:4
#Enter 'b' value:3
#After swapping
#a = 3
#b = 4
#Enter 'a'value:2
#Enter 'b' value:3
#After swapping by tuple unpacking i.e a,b=b,a
#a = 3
#b = 2


