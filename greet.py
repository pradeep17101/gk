#name=T.Pradeep
#lab=07
#task=01
#program=greet the user
# greet.py

import sys

if len(sys.argv) > 1:
    print("Hello,", sys.argv[1] + "!")
else:
    print("Please enter a name.")