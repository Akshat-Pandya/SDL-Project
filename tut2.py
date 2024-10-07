#Chapter 2 Variables and Datatypes 

#Categories of Variables - 
'''
1)Integer  -1,2,13,121,41,45,356,6,0 
2)Floating point - 12.4232,1212.1313,1212.121
3)String - "A sequence of characters" / "" / '' / '''''''
4)Boolean - True/False
5)None - Similar to null it denotes That nothing is stored in a variable It is similar to null in java or CPP
'''

#Arithematic operator - + , - ,* ,/,etc.  Binary operators
#Assignment operators : = , += , -= etc. Binary operator

a=10 # a=a+5
b=20
sum=a+b
print("The sum is ",sum)

a=123.121
print(type(a))


# Escape Sequence in Python
a="32"
b=int(a)
print("Line 1\'Line 2")

a=input("Enter your name : ") # take a string as input from the keyboard
print("Hello",a)

a=float(input("Enter a number : "))
print("The value of number : ",a)