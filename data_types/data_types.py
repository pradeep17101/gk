#name=T.Pradeep
#lab= Part A:Datatypes
#task=Integers,strings&Booleans

#Task A1.1
age = 21
current_year = 2026
birth_year = current_year - age

print("Type of age:", type(age))
print("Type of current_year:", type(current_year))
print("Type of birth_year:", type(birth_year))
print("Age in 2050:", 2050 - birth_year)

#Output:
#Type of age: <class 'int'>
#Type of current_year: <class 'int'>
#Type of birth_year: <class 'int'>
#Age in 2050: 45

#Task A1.2
x = 17
y = 5

print(x // y)   # Integer division
print(x % y)    # remainder
print(x ** 2)   # Exponent

#Output:
#3
#2
#289 


#task A2.1
#strings

first = "Ada"
last = "Lovelace"

full_name = first + " " + last

print("Uppercas:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Title Case:", full_name.title())

print("Length:", len(full_name))

print("First charcter:", full_name[0])
print("Last character:", full_name[-1])

#Output:
#Uppercase: ADA LOVELACE
#Lowercase: ada lovelace
#Title Case: Ada Lovelace
#Length: 12
#First character: A
#Last character: e


# Task A2.2

space_position = full_name.index(" ")
first_name_only = full_name[:space_position]
print("First name:", first_name_only)

#Output:
#First name: Ada


#task A3

# Boolean variables
is_raining = True
has_umbrella = False

# Print the type of the variables
print(type(is_raining))
print(type(has_umbrella))

# Logical operations
print(is_raining and has_umbrella)
print(is_raining or has_umbrella)
print(not is_raining)

# Verify that bool is a subtype of int
print(True + True)
print(False * 5)

#Output:
#<class 'bool'>
#<class 'bool'>
#False
#True
#False
#2
#0
