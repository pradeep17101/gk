#name=T.Pradeep
#lab=06
#task=02
#program=Nested for loop to print Even or Odd   

# Nested for loop to print Even or Odd
for i in range(1, 2):      # Outer loop
    for num in range(1, 11):   # Inner loop
        if num % 2 == 0:
            print(num, "- Even")
        else:
            print(num, "- Odd")

#Output:
#1 - Odd
#2 - Even
#3 - Odd
#4 - Even
#5 - Odd
#6 - Even
#7 - Odd
#8 - Even
#9 - Odd
#10 - Even
