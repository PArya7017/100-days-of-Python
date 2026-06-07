#                   LISTS
# You can create a simple collection of ordered items using a Python list.

fruits=["Cherry","Apple","Pear"]
fruits[0]="cherri"
print(fruits)
# want to add one item at end of lists 
fruits.append("Mango") #append()
print(fruits)

# want to add multiple items at the end of lists
fruits.extend(["banana","orange","guava"]) # in extend() we have to put all item inside["",""]
print(fruits)
print(fruits[3]) #positive index
print(fruits[-5]) #negative index
