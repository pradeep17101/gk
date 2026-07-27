import keyword
def is_valid_identifier(name):
    if name == "":
        return False
    if not (name[0].isalpha() or name[0] == "_"):
        return False

    for i in name:
        if not (i.isalnum() or i == "_"):
            return False

    if keyword.iskeyword(name):
        return False

    return True

name = input("Enter a name: ")

if is_valid_identifier(name):
    print("Valid Identifier")
else:
    print("Invalid Identifier")
