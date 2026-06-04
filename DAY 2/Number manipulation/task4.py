#                   Flooring a Number
# You can floor a number or remove all decimal places using the int() function which converts a floating point number (with decimal places) into an integer (whole number).

# int(3.738492) # Becomes 3

bmi = 84 / 1.65 ** 2
# without flooring a number
print(bmi)
# flooring a number
print(int(bmi))
#rounding a number
print(round(bmi))
# Rounding only to 2 decimal places
score=123.4567
print(round(score,2))

#                   Rounding a Number
# However, if you want to round a decimal number to the nearest whole number using the traditional mathematical way, where anything over .5 rounds up and anything below rounds down. Then you can use the python round() function.

print(round(3.738492)) # Becomes 4

print(round(3.14159)) # Becomes 3

print(round(3.14159, 2)) # Becomes 3.14

#                   Assignment Operators
# Assignment operators such as the addition assignment operator += will add the number on the right to the original value of the variable on the left and assign the new value to the variable.
# +=
score=99
score +=1
print(score)
# -=
score=100
score-=1
print(score)
# *=
score=50
score*=2
print(score)
# /=
score=99
score/=3
print(score)

#                   f-strings
# In Python, we can use f-strings to insert a variable or an expression into a string.
score=100
height=1.7
is_winning=True
print(f"your score = {score}, height is = {height} and your winning is {is_winning}")
