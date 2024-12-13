# String is a sequence of characters with each character having an index number 
# starting from 0 at the left. 
# ways of representation in python
s="string"
s='string'
s="""string"""
s='''string'''

# display character at index 1
print(s[1])

# string slicing : Process of extracting a part of the string from a string
sliced=s[0:4] # start from index 0 and go upto index 3
print(sliced)

# useful methods :
# Length by len(str) Note : This is not a method of string class it is a general function
# Convert string to uppercase by s.upper()
# Convert string to lowercase by s.lower()
# trim the string by s.strip() 
# trim the string only from left by s.lstrip() 
# trim the string only from right by s.rstrip() 
# replace one substring with another s.replace("one substring","another substring")
# similar to index() in java there is find() which return the index of a substring s.find("substring")
# convert to camel case by s.captalize() eg. hello world to Hello World
# count the number of occurences of a substring/character in a string by s.count("substring/character")


# check if string starts with "x" by s.startswith("x")
# check if string ends with "x" by s.endswith("x")


# check if all chars in string are digits by s.isdigit()
# check if all chars in string are alohabets by s.isalpha()
# check if all chars in string are whitespaces by s.isspace()

# Check if the substring is a part of given string : 
# Method 1 : Using the in Keyword
# if substring in string:
#     print("Substring found!")
# else:
#     print("Substring not found.")

# Method 2 : Using the fing function of string class : it returns -1 if index is not found 
# if string.find(substring) != -1:
#     print("Substring found!")
# else:
#     print("Substring not found.")
