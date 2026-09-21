#Name=T.Pradeep
#lab=04
#roll no=25341a05k1
#task=Dictionaries


#C1. Creating, Adding, and Replacing Values
#1.Dictionary of 5 students
students = {
    101: "Rahul",
    102: "Ravi",
    103: "Sita",
    104: "Anu",
    105: "Kiran"
}

print("1. Students:", students)

# Output:
# 1. Students: {101: 'Rahul', 102: 'Ravi', 103: 'Sita',
# 104: 'Anu', 105: 'Kiran'}


# 2. Add 3 new key-value pairs
students[106] = "Arun"
students[107] = "Priya"
students[108] = "Vijay"

print("2. After adding:", students)

# Output:
# 2. After adding: {101: 'Rahul', 102: 'Ravi', 103: 'Sita',
# 104: 'Anu', 105: 'Kiran', 106: 'Arun',
# 107: 'Priya', 108: 'Vijay'}


# 3. Update an existing value
marks = {
    "Maths": 80,
    "Physics": 75,
    "Chemistry": 85
}

print("3. Before update:", marks)

marks["Physics"] = 90

print("After update:", marks)

# Output:
# 3. Before update: {'Maths': 80, 'Physics': 75, 'Chemistry': 85}
# After update: {'Maths': 80, 'Physics': 90, 'Chemistry': 85}


# 4. Create dictionary using zip()
keys = ["name", "age", "city"]
values = ["Pradeep", 20, "Hyderabad"]

person = dict(zip(keys, values))

print("4. Dictionary:", person)

# Output:
# 4. Dictionary: {'name': 'Pradeep', 'age': 20, 'city': 'Hyderabad'}


# 5. Nested dictionary of 3 employees
employees = {
    1: {"name": "Ravi", "department": "IT", "salary": 30000},
    2: {"name": "Sita", "department": "HR", "salary": 35000},
    3: {"name": "Arun", "department": "Sales", "salary": 32000}
}

print("5. Employees:", employees)

# Output:
# 5. Employees: {1: {'name': 'Ravi', 'department': 'IT', 'salary': 30000},
# 2: {'name': 'Sita', 'department': 'HR', 'salary': 35000},
# 3: {'name': 'Arun', 'department': 'Sales', 'salary': 32000}}


# C2. Operations on Dictionaries

# 6. Print keys, values and key-value pairs
student = {
    "name": "Pradeep",
    "age": 20,
    "course": "B.Tech"
}

print("6. Keys:")
for key in student.keys():
    print(key)

print("Values:")
for value in student.values():
    print(value)

print("Key-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Output:
# 6. Keys:
# name
# age
# course
# Values:
# Pradeep
# 20
# B.Tech
# Key-Value pairs:
# name : Pradeep
# age : 20
# course : B.Tech


# 7. Remove using pop() and safely check using get()
data = {
    "name": "Ravi",
    "age": 21,
    "city": "Hyderabad"
}

data.pop("age")

print("7. After pop:", data)

result = data.get("salary", "Key not found")
print(result)

# Output:
# 7. After pop: {'name': 'Ravi', 'city': 'Hyderabad'}
# Key not found


# 8. Check whether a key exists
student = {
    "name": "Pradeep",
    "age": 20
}

if "name" in student:
    print("8. Name:", student["name"])
else:
    print("Key does not exist")

# Output:
# 8. Name: Pradeep


# 9. Merge two dictionaries using update() and | operator
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print("9. Using update():", dict1)

dict3 = {"a": 1, "b": 2}
merged = dict3 | dict2
print("Using | operator:", merged)

# Output:
# 9. Using update(): {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Using | operator: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# 10. Find highest and lowest price
items = {
    "Pen": 10,
    "Book": 100,
    "Bag": 500,
    "Pencil": 5
}

highest = max(items, key=items.get)
lowest = min(items, key=items.get)

print("10. Highest price:", highest, items[highest])
print("Lowest price:", lowest, items[lowest])

# Output:
# 10. Highest price: Bag 500
# Lowest price: Pencil 5


# 11. Count frequency of each character
text = "hello"

frequency = {}

for ch in text:
    frequency[ch] = frequency.get(ch, 0) + 1

print("11. Character frequency:", frequency)

# Output:
# 11. Character frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


# 12. Dictionary comprehension - cubes from 1 to 10
cubes = {x: x**3 for x in range(1, 11)}

print("12. Cubes:", cubes)

# Output:
# 12. Cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125,
# 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}