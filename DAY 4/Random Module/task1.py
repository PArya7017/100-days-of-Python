#                   Random Module
#           Pseudorandom Number Generators
# Computers are not random, because they are built with circuits and switches. But randomness is very important when building software, especially games. It would be really boring if every move in a video game was pre-determined.

# RANDINT
import random
num=random.randint(1,10)
print(num)

# RANDOM
import random
num1=random.random()
print(num1)

# UNIFORM
import random
num3=random.uniform(1,10)
print(num3)

# MODULE
import random
import my_module #here we have to write file name as i used here my_module file in another file 
print(my_module.fav_num)