#Name=T.Pradeep
#lab=04
#roll no=25341a05k1
#task=sets

# D1. Creating Sets

#1. Create a set with duplicates
s = {10, 20, 30, 20, 40, 50, 10, 60}

print("1. Set:", s)

# Output:
# 1. Set: {10, 20, 30, 40, 50, 60}
# Duplicates are automatically removed.


#2. Create set from a list and a string
my_list = [1, 2, 2, 3, 4, 4, 5]
my_string = "hello"

set1 = set(my_list)
set2 = set(my_string)

print("2. Set from list:", set1)
print("Set from string:", set2)

# Output:
# 2. Set from list: {1, 2, 3, 4, 5}
# Set from string: {'h', 'e', 'l', 'o'}


#3. Add single and multiple elements
s = {1, 2, 3}

s.add(4)
print("After add():", s)

s.update([5, 6, 7])
print("After update():", s)

# Output:
# 3. After add(): {1, 2, 3, 4}
# After update(): {1, 2, 3, 4, 5, 6, 7}


# D2. Operations on Sets
# 4. Union, intersection, difference and symmetric difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("4. Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Symmetric Difference:", A ^ B)

# Output:
# 4. Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Difference: {1, 2, 3}
# Symmetric Difference: {1, 2, 3, 6, 7, 8}


# 5. Check subset and superset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

print("5. A is subset of B:", A.issubset(B))
print("B is superset of A:", B.issuperset(A))

# Output:
# 5. A is subset of B: True
# B is superset of A: True


# 6. Remove using remove() and discard()
s = {10, 20, 30, 40}

s.remove(20)
print("6. After remove():", s)

s.discard(50)
print("After discard():", s)

# remove() gives an error if the element does not exist.
# discard() does not give an error if the element does not exist.

# Output:
# 6. After remove(): {10, 30, 40}
# After discard(): {10, 30, 40}


# 7. Check whether two sets are disjoint
A = {1, 2, 3}
B = {4, 5, 6}

print("7. Are sets disjoint?", A.isdisjoint(B))

# Output:
# 7. Are sets disjoint? True


# 8. Unique elements and sorted list
numbers = [5, 2, 3, 2, 5, 1, 4, 3, 1]

unique = set(numbers)
sorted_list = sorted(unique)

print("8. Unique elements:", unique)
print("Sorted list:", sorted_list)

# Output:
# 8. Unique elements: {1, 2, 3, 4, 5}
# Sorted list: [1, 2, 3, 4, 5]


# 9. Set comprehension for squares of odd numbers
squares = {x**2 for x in range(1, 21) if x % 2 != 0}

print("9. Squares of odd numbers:", squares)

# Output:
# 9. Squares of odd numbers:
# {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}