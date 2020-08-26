#Remember import random function here:
import random

my_list = [4,5,734,43,45]

#The magic is here:

for i in range(1,11):
    radd_ten = random.randint(1, 100)
    my_list.append(radd_ten)


print(my_list)