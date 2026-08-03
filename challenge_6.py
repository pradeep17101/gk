#name=T.Pradeep
#lab=06
#task=challenge 6
#program=Three levels of nested indentation
# Three levels of nested indentation
# for -> if -> for

for i in range(1, 6):
    if i > 0:
        for j in range(i):
            print("*", end="")
    print()

#Output:
#*
#**
#***
#****
#*****
