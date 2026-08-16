#Name=T.Pradeep
#lab=03
#task=Conditional statements

#Task 1: Check if a number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
# Output:
# Enter a number: 25
# Positive

#task 2: Check if a year is a leap year
year = int(input("Enter a year: "))
if year % 400 == 0:
    print("Leap year")
elif year % 100 == 0:
    print("Not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
# Output:
# Enter a year: 2024
# Leap year

#task 3: Check if a triangle is valid and its type
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
# Output:
# Enter first side: 5
# Enter second side: 5
# Enter third side: 5
# Equilateral triangle

#task 4: Find the largest of three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print("Largest number:", largest)
# Output:
# Enter first number: 25
# Enter second number: 45
# Enter third number: 30
# Largest number: 45.0

#task 5: Check if a character is a vowel, consonant, digit, or special symbol
marks = float(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Grade F")
# Output:
# Enter marks: 85
# Grade B

#task 6: Check if a character is a vowel, consonant, digit, or special symbol
ch = input("Enter a character: ")
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")
# Output:
# Enter a character: A
# Vowel

#task 7: Check if a date is valid
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))
if month < 1 or month > 12:
    print("Invalid date")
else:
    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            max_days = 29
        else:
            max_days = 28
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        max_days = 31
    if day >= 1 and day <= max_days:
        print("Valid date")
    else:
        print("Invalid date")
# Output:
# Enter year: 2024
# Enter month: 2
# Enter day: 29
# Valid date
