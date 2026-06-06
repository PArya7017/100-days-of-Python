#               Nesting and Elif
# You can put if/else statements inside other if/else statements. This is known as nesting.

print("Welcome to Rollercoaster ride!")
height= int(input("Enter your height in cm? "))
print(height)
if height >=120:
    print("Hurray, you can ride!")
    age= int(input("Enter your age please: "))
    if age<=12:
        print("Please pay $5")
    elif age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you can't :/")
