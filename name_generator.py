from random import *


#Create the list of words you want to choose from.
greys_anatomy= ["meredith", "derek", "callie", "christina", "alex", "owen",
"miranda", "jackson","april", "arizona", "richard", "jo", "mark", "amelia",
"lexie", "stephanie", "maggie"]
x = randint(0, len(greys_anatomy)-1)
print (greys_anatomy[x])
