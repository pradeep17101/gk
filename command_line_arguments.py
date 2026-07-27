#Name: T.Pradeep
#Lab:07
#Task:02
#Program:Adding of two numbers using command line arguments
import sys
if len(sys.argv)==3:
    n1=int(sys.argv[1]);n2=int(sys.argv[2])
    print("n1=",n1)
    print("n2=",n2)
    print("sum=",n1+n2)
else:
    print("wrong number of arguments")

#Output:
#wrong number of arguments
