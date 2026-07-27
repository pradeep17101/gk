#name=T.Pradeep
#lab=07 
#task=challenge 7
#program=Write a program to accept two numbers as command line arguments and print their sum
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num1", type=int, default=0)
parser.add_argument("--num2", type=int, default=0)

args = parser.parse_args()

print("Sum =", args.num1 + args.num2)

#Output:
#Sum = 0
