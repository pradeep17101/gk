#name=T.Pradeep
#lab=05
#task=04
#program=Write a program to input multiple values in single line and find sum of them
# Input numbers in one line
numbers = input("Enter numbers separated by spaces: ")
# Convert to integers and find sum
numbers = list(map(int, numbers.split()))
print("Sum =", sum(numbers))

#Output:
#Enter numbers separated by spaces: 2
#Sum = 2
