#Name=T.Pradeep
#rollno=5k1
#lab=03
#task=Pattern programs

#task 1: Print a right-angled triangle pattern of stars
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
  for j in range(1, i + 1):
        print("*", end=" ")
    print()
# Output:
# Enter number of rows: 5
# *
# * *
# * * *
# * * * *
# * * * * *

#task 2: Print an inverted right-angled triangle pattern of stars
n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 5
# * * * * *
# * * * *
# * * *
# * *
# *

#task 3: Print a pyramid pattern of stars
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 5
# *
# * *
# * * *
# * * * *
# * * * * *

#task 4: Print a diamond pattern of stars
n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 5
# * * * * *
# * * * *
# * * *
# * *
# *

#task 5: Print a hollow square pattern of stars
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()

# Output:
# Enter number of rows: 4
#       *
#     * * *
#   * * * * *
# * * * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *

#task 6: Print a right-angled triangle pattern of numbers
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

# Output:
# Enter number of rows: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

#task 7: Print a pyramid pattern of numbers
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Output:
# Enter number of rows: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#task 8: Print a diamond pattern of numbers
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()

# Output:
# Enter number of rows: 5
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

#task 9: Print a right-angled triangle pattern of alphabets
n = int(input("Enter number of rows: "))

for i in range(n):
    ch = chr(65 + i)

    for j in range(i + 1):
        print(ch, end=" ")

    print()

# Output:
# Enter number of rows: 5
# A
# B B
# C C C
# D D D D
# E E E E E


#task 10: Print a pyramid pattern of alphabets
n = int(input("Enter size of square: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Output:
# Enter size of square: 5
# * * * * *
# *       *
# *       *
# *       *
# * * * * *

#task 11: Print a hollow diamond pattern of stars
n = int(input("Enter number of rows: "))

# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Output:
# Enter number of rows: 4
#       *
#     *   *
#   *       *
# *           *
#   *       *
#     *   *
#       *

#task 12: Print a number pyramid pattern
n = int(input("Enter number of rows: "))

num = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

# Output:
# Enter number of rows: 5
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

#task 13: Print a butterfly pattern of stars
n = int(input("Enter number of rows: "))

# Upper half
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Lower half
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")

    for j in range(2 * (n - i)):
        print(" ", end=" ")

    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Output:
# Enter number of rows: 4
# *             *
# * *         * *
# * * *     * * *
# * * * * * * * *
# * * * * * * * *
# * * *     * * *
# * *         * *
# *             *


