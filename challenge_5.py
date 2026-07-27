#Name: T.Pradeep
#Lab:05
#Task:challenge 5
#Program:average marks rounded to 2 decimals
# Enter 3 subject marks in one line
marks = list(map(int, input("Enter 3 marks: ").split()))
# Calculate average
average = sum(marks) / 3
# Print average with 2 decimal places
print("Average = {:.2f}".format(average))
