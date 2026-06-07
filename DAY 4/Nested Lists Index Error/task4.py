

# Nested Lists
fruits=["Cherry", "Apple", "Pear"]
vegetables=["Cucumber", "Kale", "Spinnach"]
grocery=[fruits,vegetables]
print(grocery)

# IndexError
# fruits=["appple","banana","cherry"]
# print(fruits[3])
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])