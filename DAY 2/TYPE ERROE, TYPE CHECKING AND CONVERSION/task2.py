                        # Type error, type checking and conversion

# TypeError
# len(1234) // We are using here wrong datatype Because you can only give the len() function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

# PAUSE 1. Fix the len() function so it has no more warnings or errors.
len("hello") # here there is no type error

# Type Checking
# You can check the data type of any value or variable in python using the type() function.

# PAUSE 2. Write out 4 type checks to print all 4 data types
print(type("Tomya"))
print(type(7017))
print(type(3.14154))
print(type(True))

# Type conversion
# You can convert data into different data types using special functions. e.g.

# float()
# int()
# str()

# PAUSE 3. Make this line of code run without errors
# print("Number of letters in your name: " + len(input("Enter your name")))

print("Number of letters in your name: "+str(len(input("Enter your name: "))))

# Some examples 
# Integer -> String
age=22
print("My age is: "+ str(age))
# kyuki string + integer ko jod nahi skte
# str+str is ok

# String->Integer
num1="10"
num2="20"
print(int(num1)+int(num2))

# Integer -> Float
marks=89
print(float(marks))

# Float-> Integer
temp=100.12
print(int(temp))

# String->Float
height="5.7"
print(float(height))

# Number input from user

num1=int(input("enter your number 1: "))
num2=int(input("enter your number 2: "))
print(num1+num2)