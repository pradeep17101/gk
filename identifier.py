#Name=T.Pradeep
#lab=1
#task=1
#Program=five valid identifiers	of different kinds: a variable,	a constant-style name, a function name,	a class name, and a name using an underscore.


number = 10
MAX_VALUE = 100
def greet():
    print("Function Name: greet")
class Student:
    pass
user_name = "Pradeep"
print("Variable:", number)
print("Constant-style Name:", MAX_VALUE)
print("Class Name:", Student.__name__)
print("Underscore Name:", user_name)
greet()


#Output:
#Variable: 10
#Constant-style Name: 100
#Class Name: Student
#Underscore Name: Pradeep
#Function Name: greet
