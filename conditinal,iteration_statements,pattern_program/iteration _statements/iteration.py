#Name=T.Pradeep
#rollno=5k1
#lab=03
#task=Iteration  statements

#task 1: Print numbers from 1 to N
n = int(input("Enter N: "))
i = 1
while i <= n:
    print(i)
    i += 1
# Output:
# Enter N: 5
# 1
# 2
# 3
# 4
# 5

#task 2: Print even numbers from 1 to N
n = int(input("Enter a number: "))

temp = abs(n)
sum_digits = 0
count = 0
while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10
if count > 0:
    average = sum_digits / count
else:
    average = 0
print("Sum of digits:", sum_digits)
print("Average of digits:", average)
# Output:
# Enter a number: 1234
# Sum of digits: 10
# Average of digits: 2.5

#task 3: Reverse a number
n = int(input("Enter an integer: "))
temp = abs(n)
reverse = 0
while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10
if n < 0:
    reverse = -reverse
print("Reversed number:", reverse)
# Output:
# Enter an integer: 1234
# Reversed number: 4321

#task 4: Check if a number is a palindrome
n = int(input("Enter a number: "))
original = n
temp = n
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
# Output:
# Enter a number: 121
# Palindrome

#task 5: Fibonacci series up to N terms
n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
# Output:
# Enter the number of terms: 7
# 0 1 1 2 3 5 8

#task 6: Print multiplication table of a number
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
# Output:
# Enter a number: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

#task 7: Calculate factorial of a number
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)
# Output:
# Enter a number: 5
# Factorial: 120

#task 8: Count vowels, consonants, digits, and spaces in a string
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
# Output:
# Enter a string: Hello World 123
# Vowels: 3
# Consonants: 7
# Digits: 3
# Spaces: 2

#task 9: Check if a number is prime
n = int(input("Enter a number: "))

if n <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")
# Output:
# Enter a number: 17
# Prime number

#task 10: Print all prime numbers in a given range
start = int(input("Enter the lower limit: "))
end = int(input("Enter the upper limit: "))

print("Prime numbers:")

for n in range(start, end + 1):
    if n > 1:
        is_prime = True

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print(n, end=" ")
# Output:
# Enter the lower limit: 10
# Enter the upper limit: 30
# Prime numbers:
# 11 13 17 19 23 29


