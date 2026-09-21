#Name=T.Pradeep
#Lab=05
#roll no=25341a05k1

# STRING PRACTICE PROGRAMS

# 1. Find length of a string
s = input("1. Enter a string: ")
print("Length:", len(s))

#Output:
# Enter a string: Python
# Length: 6


# 2. Reverse without slicing and with slicing
s = "Python"

reverse = ""
for ch in s:
    reverse = ch + reverse

print("2. Without slicing:", reverse)
print("With slicing:", s[::-1])

# Output:
# 2. Without slicing: nohtyP
# With slicing: nohtyP


# 3. Check palindrome
s = "madam"

if s == s[::-1]:
    print("3. Palindrome")
else:
    print("Not a palindrome")

# Output:
# 3. Palindrome


# 4. Uppercase and lowercase
s = "Python Programming"

print("4. Uppercase:", s.upper())
print("Lowercase:", s.lower())

# Output:
# 4. Uppercase: PYTHON PROGRAMMING
# Lowercase: python programming


# 5. Count vowels, consonants, digits and spaces
s = "Hello World 123"

vowels = consonants = digits = spaces = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("5. Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

# Output:
# 5. Vowels: 3
# Consonants: 7
# Digits: 3
# Spaces: 2


# 6. Count occurrence of a character
s = "banana"
ch = "a"

print("6. Count:", s.count(ch))

# Output:
# 6. Count: 3


# 7. Remove all whitespace
s = "Hello World Python"

result = s.replace(" ", "")

print("7. Without spaces:", result)

# Output:
# 7. Without spaces: HelloWorldPython


# 8. Replace a character/word
s = "I like Java"

result = s.replace("Java", "Python")

print("8. After replacement:", result)

# Output:
# 8. After replacement: I like Python


# 9. Concatenate without + operator
s1 = "Hello"
s2 = "World"

result = " ".join([s1, s2])

print("9. Concatenated:", result)

# Output:
# 9. Concatenated: Hello World


# 10. Swap case
s = "Hello Python"

print("10. Swapped case:", s.swapcase())

# Output:
# 10. Swapped case: hELLO pYTHON


# 3. SLICING & INDEXING

# 11. First and last characters
s = "Python"

print("11. First character:", s[0])
print("Last character:", s[-1])

# Output:
# 11. First character: P
# Last character: n


# 12. Print every second character
s = "PythonProgramming"

print("12. Every second character:", s[::2])

# Output:
# 12. Every second character: PtoPormig


# 13. Check substring
s = "Python Programming"

if "Python" in s:
    print("13. Substring exists")
else:
    print("Substring does not exist")

# Output:
# 13. Substring exists


# 14. First and last occurrence of a character
s = "banana"
ch = "a"

print("14. First occurrence:", s.find(ch))
print("Last occurrence:", s.rfind(ch))

# Output:
# 14. First occurrence: 1
# Last occurrence: 5


# 4. WORDS & SENTENCES


# 15. Count words in a sentence
sentence = "Python is very easy to learn"

words = sentence.split()

print("15. Number of words:", len(words))

# Output:
# 15. Number of words: 6


# 16. Find longest word
sentence = "Python programming is interesting"

words = sentence.split()
longest = max(words, key=len)

print("16. Longest word:", longest)

# Output:
# 16. Longest word: programming


# 17. Reverse order of words
sentence = "Python is easy"

words = sentence.split()
result = " ".join(words[::-1])

print("17. Reversed words:", result)

# Output:
# 17. Reversed words: easy is Python


# 18. Capitalize first letter of every word without title()
sentence = "python programming language"

words = sentence.split()
result = ""

for word in words:
    result += word[0].upper() + word[1:] + " "

print("18. Title case:", result.strip())

# Output:
# 18. Title case: Python Programming Language


# 19. Check whether two strings are anagrams
s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("19. Anagrams")
else:
    print("Not anagrams")

# Output:
# 19. Anagrams


# 5. ADVANCED

# 20. Remove duplicate characters
s = "programming"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("20. Without duplicates:", result)

# Output:
# 20. Without duplicates: progamin


# 21. Check digits, alphabets or alphanumeric
s = "Python123"

if s.isdigit():
    print("21. Contains only digits")
elif s.isalpha():
    print("Contains only alphabets")
elif s.isalnum():
    print("Contains alphabets and digits")

# Output:
# 21. Contains alphabets and digits


# 22. Find duplicate characters and their counts
s = "programming"
duplicates = {}

for ch in s:
    if s.count(ch) > 1:
        duplicates[ch] = s.count(ch)

print("22. Duplicate characters:", duplicates)

# Output:
# 22. Duplicate characters: {'r': 2, 'g': 2, 'm': 2}


# 23. String to list and list back to string
s = "Python"

char_list = list(s)
print("23. List:", char_list)

new_string = "".join(char_list)
print("String:", new_string)

# Output:
# 23. List: ['P', 'y', 't', 'h', 'o', 'n']
# String: Python


# 24. Check valid Python identifier
s = "student_name"

if s.isidentifier():
    print("24. Valid identifier")
else:
    print("Invalid identifier")

# Output:
# 24. Valid identifier


# 25. Own version of find() and count()
s = "banana"
target = "a"

# Own find()
position = -1

for i in range(len(s)):
    if s[i] == target:
        position = i
        break

# Own count()
count = 0

for ch in s:
    if ch == target:
        count += 1

print("25. First position:", position)
print("Count:", count)

# Output:
# 25. First position: 1
# Count: 3
