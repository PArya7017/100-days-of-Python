# PAUSE 1 -     Heads or Tails

# Create a coin flip program using what you have learnt about randomisation in Python. It should randomly print "Heads" or "Tails" everytime it is run.

import random
choose_Head_Tail=random.randint(0,1)
print(choose_Head_Tail)
if choose_Head_Tail==0:
    print("Heads!, I win :)")
else:
    print("Tails!, I win :)")