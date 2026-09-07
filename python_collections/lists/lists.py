#Name=T.Pradeep
#lab=04
#task name=Python collections

Task1=Lists

###Programs A1 =Creating Lists
#1. Create a list of 10 integers and print the list and length
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("List:", numbers)
print("Length:", len(numbers))
#output:
#List: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#Length: 10

#2. List containing different data types
data = [10, 3.14, "Hello", True, [1, 2, 3]]

for item in data:
    print(item, type(item))
#Output:
#10 <class 'int'>
#3.14 <class 'float'>
#Hello <class 'str'>
#True <class 'bool'>
#[1, 2, 3] <class 'list'>


#3. Create an empty list and add 5 elements
my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

print(my_list)
#Output:
#[10, 20, 30, 40, 50]


###Programs A2 =Accessing List Elements
#4. Print first, last, and index 3 elements
fruits = ["Apple", "Banana", "Mango", "Orange",
          "Grapes", "Pineapple", "Papaya", "Watermelon"]

print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Element at index 3:", fruits[3])
#Output:
#First element: Apple
#Last element: Watermelon
#Element at index 3: Orange


5. Print elements with their index using enumerate()
numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    print(index, value)
#Output:
#0 10
#1 20
#2 30
#4 50
    

###Program A3= Slicing Lists
#6. Print first 3, last 3, and alternate elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("First 3:", numbers[:3])
print("Last 3:", numbers[-3:])
print("Alternate:", numbers[::2])

#Output:
#First 3: [1, 2, 3]
#Last 3: [8, 9, 10]
#Alternate: [1, 3, 5, 7, 9]

7. Reverse a list using slicing
numbers = [1, 2, 3, 4, 5]

reverse = numbers[::-1]
print("Reversed list:", reverse)
#Output:
#Reversed List = [5, 4, 3, 2, 1]

8. Extract middle 4 elements from a list of 12 elements
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print("Middle 4 elements:",numbers[4:8])

#Output:
#Middle 4 elements: [5, 6, 7, 8]

###Program A4= Negative Indices

9. Print last, second-last, and last 3 elements
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Last element:", numbers[-1])
print("Second-last element:", numbers[-2])
print("Last 3 elements:", numbers[-3:])
#Output:
#Last element: 70
#Second-last element: 60
#Last 3 elements: [50, 60, 70]

10. Reverse a list using negative step
numbers = [1, 2, 3, 4, 5, 6]

print("Reverse:", numbers[::-1])
#Output:
#Reverse: [6, 5, 4, 3, 2, 1]

###Program A5= List Methods

11. Demonstrate list methods
numbers = [5, 2, 8, 2, 10]
numbers.append(20)
print("After append:", numbers)
numbers.insert(1, 15)
print("After insert:", numbers)
numbers.extend([25, 30])
print("After extend:", numbers)
numbers.remove(2)
print("After remove:", numbers)
numbers.pop()
print("After pop:", numbers)
numbers.sort()
print("After sort:", numbers)
numbers.reverse()
print("After reverse:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 15:", numbers.index(15))

#Output:
#After append: [5, 2, 8, 2, 10, 20]
#After insert: [5, 15, 2, 8, 2, 10, 20]
#After extend: [5, 15, 2, 8, 2, 10, 20, 25, 30]
#After remove: [5, 15, 8, 2, 10, 20, 25, 30]
#After pop: [5, 15, 8, 2, 10, 20, 25]
#After sort: [2, 5, 8, 10, 15, 20, 25]
#After reverse: [25, 20, 15, 10, 8, 5, 2]
#Count of 2: 1
#Index of 15: 2

#12. Remove duplicate elements from a list without using set()
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
duplicate = []
for num in numbers:
    if num not in duplicate:
        duplicate.append(num)
print("Original list:", numbers)
print("List without duplicates:", duplicate)
#Output:
#Original list: [10, 20, 10, 30, 20, 40, 30, 50]
#List without duplicates: [10, 20, 30, 40, 50]


#13. Find maximum, minimum, and sum without using max(), min(), or sum()
numbers = [10, 25, 5, 40, 15]
maximum = numbers[0]
minimum = numbers[0]
total = 0
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

    total += num
print("List:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
#Output:
#List: [10, 25, 5, 40, 15]
#Maximum: 40
#Minimum: 5
#Sum: 95

#14. Merge two lists and sort the combined list in descending order
list1 = [10, 30, 20]
list2 = [50, 40, 60]
merged_list = list1 + list2
merged_list.sort(reverse=True)
print("List 1:", list1)
print("List 2:", list2)
print("Merged list in descending order:", merged_list)
#Output:
#List 1: [10, 30, 20]
#List 2: [50, 40, 60]
#Merged list in descending order: [60, 50, 40, 30, 20, 10]



###Program A6=List Comprehensions

#15. Generate a list of squares of numbers from 1 to 20
squares = [x ** 2 for x in range(1,21)]
print("Squares from 1 to 20:",squares)
#Output:
#Squares from 1 to 20: [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]

#16. Create a list of all even numbers between 1 and 50
even_numbers = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers between 1 and 50:", even_numbers)
#Output:
#Even numbers between 1 and 50: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

#17. Create a list containing words with more than 4 letters
words = ["apple", "cat", "banana", "dog", "orange", "book"]
long_words = [word for word in words if len(word) > 4]
print("Original words:", words)
print("Words with more than 4 letters:", long_words)
#Output:
#Original words: ['apple', 'cat', 'banana', 'dog', 'orange', 'book']
#Words with more than 4 letters: ['apple', 'banana', 'orange']

#18. Create a 3x3 matrix containing numbers 1 to 9 using nested list comprehension
matrix = [[(i * 3) + j + 1 for j in range(3)] for i in range(3)]
print("3x3 Matrix:")
for row in matrix:
    print(row)
#Output:
#3x3 Matrix:
#[1, 2, 3]
#[4, 5, 6]
#[7, 8, 9]
    
#19. Replace negative numbers with 0 using list comprehension Positive numbers remain unchanged
numbers = [10, -5, 20, -10, 30, -15, 40]
result = [0 if x < 0 else x for x in numbers]
print("Original list:", numbers)
print("After replacing negative numbers:", result)
#Output:
#Original list: [10, -5, 20, -10, 30, -15, 40]
#After replacing negative numbers: [10, 0, 20, 0, 30, 0, 40]

