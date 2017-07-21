from random import *

sides = ["mashed_potatoes", "broccoli", "rice", "french_fries", "green_beans"]
main_courses= ["chicken_alfredo","salmon", "enchilada", "meatloaf", "pot_roast"]
desserts= ["ice_cream", "brownie", "creme_brule", "cheesecake", "apple_pie"]

#Generates a random integer.
x = randint(0, len(sides)-1)
y = randint (0, len(main_courses) -1)
z = randint (0, len(desserts) -1)

print (sides [x], main_courses [y], desserts [z])
