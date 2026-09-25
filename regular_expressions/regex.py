#Name=T.Pradeep
#lab=06
#task=regular_expressions

# TASK 1 — BASIC PATTERN MATCHING

import re
s="1024 requests were served in 3 seconds"
print(re.match(r"\d",s).group())
print(re.search("served",s).span())
print(bool(re.fullmatch(r"\d+","12345")))
print(bool(re.fullmatch(r"\d+","123a5")))

# OUTPUT
# 1
# (18, 24)
# True
# False


# TASK 2 — FINDING ALL MATCHES

import re
s="NASA and USA work with ISRO on important projects"
print(re.findall(r"\b[A-Z]{2,}\b",s))
for x in re.finditer(r"\b\w{7,}\b",s):
    print(x.group(),x.start())
p="apples: $3.50, bananas: $1.20, mango: $4.75"
a=re.findall(r"\$\d+\.\d+",p)
print(a)
print(len(a))

# OUTPUT
# ['NASA', 'USA', 'ISRO']
# important 23
# projects 33
# ['$3.50', '$1.20', '$4.75']
# 3


# TASK 3 — SEARCH AND REPLACE

import re
s="Contact john@example.com or mary@test.com"
print(re.sub(r"[\w.-]+@[\w.-]+\.\w+","[EMAIL HIDDEN]",s))
print(re.sub(r"(\w+),\s*(\w+)",r"\2 \1","Doe, John"))

def f(x):
    return str(int(x.group())*2)

print(re.sub(r"\d+",f,"I have 3 apples"))
print(re.subn(r"([!?])\1+",r"\1","Wait!!! What??"))

# OUTPUT
# Contact [EMAIL HIDDEN] or [EMAIL HIDDEN]
# John Doe
# I have 6 apples
# ('Wait! What?', 2)


# TASK 4 — BUILDING PATTERNS

import re
p=r"[A-Za-z_]\w*"

for x in ["_count2","2fast","total_sum"]:
    print(x,bool(re.fullmatch(p,x)))

print(re.findall(r"\b(cat|dog|bird)\b","I have a cat, dog and bird"))
print(re.findall(r"#[0-9A-Fa-f]{3}(?:[0-9A-Fa-f]{3})?","#FFAA00 #000 #ABC"))

s="2024-06-01 08:15:32 ERROR Disk full"
p=r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<level>\w+) (?P<msg>.*)"
m=re.search(p,s)
print(m.group("date"))
print(m.group("time"))
print(m.group("level"))
print(m.group("msg"))

# OUTPUT
# _count2 True
# 2fast False
# total_sum True
# ['cat', 'dog', 'bird']
# ['#FFAA00', '#000', '#ABC']
# 2024-06-01
# 08:15:32
# ERROR
# Disk full


# TASK 5.1 — EMAIL VALIDATOR

import re

def valid(x):
    return bool(re.fullmatch(r"[\w.]+@[\w.-]+\.[A-Za-z]{2,6}",x))

for x in ["a@gmail.com","abc@test.co","a@b.c","no-at-sign.com"]:
    print(x,valid(x))

# OUTPUT
# a@gmail.com True
# abc@test.co True
# a@b.c False
# no-at-sign.com False


# TASK 5.2 — PHONE NUMBER EXTRACTOR

import re

s="555-123-4567 (555) 987-6543 555.456.7890"
p=r"(?:\(\d{3}\)|\d{3})[-. ]\d{3}[-.]\d{4}"

for x in re.findall(p,s):
    x=re.sub(r"\D","",x)
    print(re.sub(r"(\d{3})(\d{3})(\d{4})",r"\1-\2-\3",x))

# OUTPUT
# 555-123-4567
# 555-987-6543
# 555-456-7890


# TASK 5.3 — DATE EXTRACTION AND REFORMATTING

import re

s="Dates: 25/09/2026, 01/10/2026 and 15/12/2026"
print(re.findall(r"(\d{2})/(\d{2})/(\d{4})",s))
print(re.sub(r"(\d{2})/(\d{2})/(\d{4})",r"\3-\2-\1",s))

# OUTPUT
# [('25', '09', '2026'), ('01', '10', '2026'), ('15', '12', '2026')]
# Dates: 2026-09-25, 2026-10-01 and 2026-12-15


# TASK 5.4 — WHITESPACE AND HTML CLEANUP

import re

def clean(s):
    s=re.sub(r"<.*?>","",s)
    return re.sub(r"\s+"," ",s).strip()

print(clean("<p>Hello   <b>World</b></p>\n Python"))

# OUTPUT
# Hello World Python


# TASK 5.5 — PASSWORD STRENGTH CHECKER

import re

def check(p):
    r=[]
    if len(p)<8:r+=["Length"]
    if not re.search("[A-Z]",p):r+=["Uppercase"]
    if not re.search("[a-z]",p):r+=["Lowercase"]
    if not re.search("\d",p):r+=["Digit"]
    if not re.search("[!@#$%^&*]",p):r+=["Symbol"]
    return r

for p in ["Abc123!x","password","ABC12345"]:
    print(p,check(p))

# OUTPUT
# Abc123!x []
# password ['Uppercase', 'Digit', 'Symbol']
# ABC12345 ['Lowercase', 'Symbol']


# TASK 6 — MINI LOG PARSER

import re

s='''[2024-06-01 08:15:32] ERROR user=jsmith msg="Disk quota exceeded"
[2024-06-01 08:16:05] INFO user=agarcia msg="Login successful"
[2024-06-01 08:17:44] WARN user=jsmith msg="High memory usage"'''

p=r'\[(?P<timestamp>.*?)\] (?P<level>\w+) user=(?P<user>\w+) msg="(?P<msg>.*?)"'
a=[x.groupdict() for x in re.finditer(p,s)]

print(a)
print("ERROR:",len(re.findall("ERROR",s)))
print("WARN:",len(re.findall("WARN",s)))
print("INFO:",len(re.findall("INFO",s)))
print(re.sub(r"user=\w+","user=<hidden>",s))

# OUTPUT
# [{'timestamp': '2024-06-01 08:15:32', 'level': 'ERROR', 'user': 'jsmith', 'msg': 'Disk quota exceeded'},
# {'timestamp': '2024-06-01 08:16:05', 'level': 'INFO', 'user': 'agarcia', 'msg': 'Login successful'},
# {'timestamp': '2024-06-01 08:17:44', 'level': 'WARN', 'user': 'jsmith', 'msg': 'High memory usage'}]
# ERROR: 1
# WARN: 1
# INFO: 1
# [2024-06-01 08:15:32] ERROR user=<hidden> msg="Disk quota exceeded"
# [2024-06-01 08:16:05] INFO user=<hidden> msg="Login successful"
# [2024-06-01 08:17:44] WARN user=<hidden> msg="High memory usage"