#Name=T.Pradeep
#lab=07
#rollNo=25341A05K1

#Task1: Simple Greeting Function

def greet(name):
    print(f"Hello, {name}! Welcome to Python.")

greet("Siddu")
greet("Ravi")
greet("Pradeep")

# Output:
# Hello, Siddu! Welcome to Python.
# Hello, Ravi! Welcome to Python.
# Hello, Pradeep! Welcome to Python.


#Task2: Simple Interest Calculator

def simple_interest(principal, rate, time):
    "Calculates and returns simple interest."
    return (principal * rate * time) / 100

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

print("Simple Interest:", simple_interest(p, r, t))

#Output:
#Enter principal:5000
#Enter rate:5
#Enter time:2
#Simple Interest:500.0


#Task3:Even or Odd Checker

def is_even(n):
    return n % 2 == 0

for i in range(5):
    n = int(input("Enter number: "))
    if is_even(n):
        print(n, "is Even")
    else:
        print(n, "is Odd")

#Output:
#Enter number: 10
#10 is Even
#Enter number: 7
#7 is Odd
#Enter number: 24
#24 is Even
#Enter number: 13
#13 is Odd
#Enter number: 8
#8 is Even


#Task4: Function Returning Multiple Values

def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
minimum, maximum, average = stats(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)

#Output:
#Minimum: 10
#Maximum: 50
#Average: 30.0


#Task5: Temperature Converter (Nested Function Calls)

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

while True:
    print("\n1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice==1:
        c = float(input("Enter Celsius: "))
        print("Fahrenheit:", celsius_to_fahrenheit(c))
    elif choice==2:
        f = float(input("Enter Fahrenheit: "))
        print("Celsius:", fahrenheit_to_celsius(f))
    elif choice==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")

#Output:
#1. Celsius to Fahrenheit
#2. Fahrenheit to Celsius
#3. Exit
#Enter choice: 1
#Enter Celsius: 25
#Fahrenheit: 77.0
#
#1. Celsius to Fahrenheit
#2. Fahrenheit to Celsius
#3. Exit
#Enter choice: 2
#Enter Fahrenheit: 98.6
#Celsius: 37.0
#
#1. Celsius to Fahrenheit
#2. Fahrenheit to Celsius
#3. Exit
#Enter choice: 3
#Exiting...
