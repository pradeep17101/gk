

#Name=T.Pradeep
#lab=Operators
#Task= types of operators
# B1. Arithmetic Operators

print(" B1. Arithmetic Operators ")
a = 23
b = 6

print("a =", a, "b =", b)
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)
print("Floor Division (//):", a // b)
print("Modulus (%):", a % b)
print("Exponent (**):", a ** b)


#Output:
#a = 23 b = 6
#Addition (+): 29
#Subtraction (-): 17
#Multiplication (*): 138
#Division (/): 3.8333333333333335
#Floor Division (//): 3
#Modulus (%): 5
#Exponent (**): 148035889
 


# B2. Comparison Operators


print(" B2. Comparison Operators ")

m = int(input("Enter m: "))
n = int(input("Enter n: "))

print("m == n :", m == n)
print("m != n :", m != n)
print("m > n  :", m > n)
print("m < n  :", m < n)
print("m >= n :", m >= n)
print("m <= n :", m <= n)

#Output:
#Enter m: 4
#Enter n: 3
#m == n : False
#m != n : True
#m > n  : True
#m < n  : False
#m >= n : True
#m <= n : False


# B3. Assignment Operators

print("B3. Assignment Operators ")

score = 50
print("Initial score =", score)

score += 10
print("After += 10 :", score)

score -= 5
print("After -= 5 :", score)

score *= 2
print("After *= 2 :", score)

score /= 3
print("After /= 3 :", score)

score //= 2
print("After //= 2 :", score)

score %= 5
print("After %= 5 :", score)

score **= 2
print("After **= 2 :", score)

#Output:
#Initial score = 50
#After += 10 : 60
#After -= 5 : 55
#After *= 2 : 110
#After /= 3 : 36.666666666666664
#After //= 2 : 18.0
#After %= 5 : 3.0
#After **= 2 : 9.0


# B4. Logical Operators


print("B4. Logical Operators")

percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance (%): "))

eligible = percentage > 75 and attendance > 90

print("Eligible for scholarship:", eligible)

#Output:
#Enter percentage: 70
#Enter attendance (%): 85
#Eligible for scholarship: False


# B5. Bitwise Operators

print("B5. Bitwise Operators ")

p = 12
q = 10

print("p =", p, "Binary:", bin(p))
print("q =", q, "Binary:", bin(q))

print("p & q =", p & q)
print("p | q =", p | q)
print("p ^ q =", p ^ q)
print("~p =", ~p)
print("p << 2 =", p << 2)
print("p >> 2 =", p >> 2)

#Output:
#p = 12 Binary: 0b1100
#q = 10 Binary: 0b1010
#p & q = 8
#p | q = 14
#p ^ q = 6
#~p = -13
#p << 2 = 48
#p >> 2 = 3


# B6. Membership Operators

print("B6. Membership Operators")

fruits = ["apple", "banana", "mango", "grape", "kiwi"]

item = input("Enter a fruit: ")

print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)

#Output:
#Enter a fruit: mango
#mango is in the list: True
#mango is not in the list: False


# B7. Identity Operators


print(" B7. Identity Operators")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)
print("list1 is not list2 :", list1 is not list2)

print("\nMemory Addresses:")
print("id(list1):", id(list1))
print("id(list2):", id(list2))
print("id(list3):", id(list3))

#Output:
#list1 == list2 : True
#list1 is list2 : False
#list1 is list3 : True
#list1 is not list2 : True

#Memory Addresses:
#id(list1): 2749230117312
#id(list2): 2749228891264
#id(list3): 2749230117312

