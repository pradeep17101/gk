#Name: T.Pradeep
#Lab:02
#Task:01
#Program:List of python keywords
import keyword
print(keyword.kwlist)
print("Total number of keywords:",len(keyword.kwlist))
print("Soft keywors:",keyword.softkwlist)
print("Total no of Soft Keywords:",len(keyword.softkwlist))

#Output:
#['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#Total number of keywords: 35
#Soft keywors: ['_', 'case', 'match', 'type']
#Total no of Soft Keywords: 4

