#Name=T.Pradeep
#lab=04
#roll no=24341a05k1

# B1. Creating Tuples

# 1. Tuple of 6 countries
countries = ("India", "USA", "Japan", "France", "Germany", "Canada")
print(countries)
print(type(countries))
print(len(countries))

# Output:
# ('India', 'USA', 'Japan', 'France', 'Germany', 'Canada')
# <class 'tuple'>
# 6


# 2. Single element tuple
t = ("India",)
print(t)
print(type(t))

# Output:
# ('India',)
# <class 'tuple'>


# 3. List to tuple and tuple to list
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)
print(my_tuple)

new_list = list(my_tuple)
print(new_list)

# Output:
# (10, 20, 30, 40)
# [10, 20, 30, 40]


# B2. Indexing and Slicing Tuples

# 4. Positive and negative indexing
t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(t[0])
print(t[5])
print(t[-1])
print(t[-10])

# Output:
# 10
# 60
# 100
# 10


# 5. First half and second half
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
print("First half:", t[:6])
print("Second half:", t[6:])

# Output:
# First half: (1, 2, 3, 4, 5, 6)
# Second half: (7, 8, 9, 10, 11, 12)


# 6. Check value in tuple
t = (10, 20, 30, 40, 50)
x = 30

if x in t:
    print("Value exists in tuple")
else:
    print("Value does not exist")

# Output:
# Value exists in tuple


# 7. Maximum, minimum and count
t = (10, 20, 30, 20, 40, 20, 50)
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Count of 20:", t.count(20))

# Output:
# Maximum: 50
# Minimum: 10
# Count of 20: 3


# B3. Operations on Tuples

# 8. Concatenation and repetition
t1 = (1, 2, 3)
t2 = (4, 5, 6)

print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 3)

# Output:
# Concatenation: (1, 2, 3, 4, 5, 6)
# Repetition: (1, 2, 3, 1, 2, 3, 1, 2, 3)


# 9. Unpacking student marks and average
marks = (80, 70, 90, 60, 100)
a, b, c, d, e = marks

average = (a + b + c + d + e) / 5
print("Average:", average)

# Output:
# Average: 80.0


# 10. Tuple immutability
t = (10, 20, 30)

try:
    t[0] = 100
except TypeError:
    print("Tuple cannot be modified")

# Output:
# Tuple cannot be modified


# 11. Nested list inside tuple
t = (10, [20, 30], 40)

t[1].append(50)
print(t)

# The tuple is immutable, but the list inside it is mutable.

# Output:
# (10, [20, 30, 50], 40)


# 12. Sort tuple
t = (50, 20, 40, 10, 30)

result = sorted(t)
print("Sorted list:", result)

# Output:
# Sorted list: [10, 20, 30, 40, 50]