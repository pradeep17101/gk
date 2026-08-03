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


#taskA1.3

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
