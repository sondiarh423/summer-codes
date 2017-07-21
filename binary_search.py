alphabet= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
"t", "u", "v", "w", "x", "y", "z"]

lenght_list = len (alphabet)
bottom = 0
top = lenght_list
target= "h"
not_found=True

while(top >= bottom):
    midpoint =int( (bottom + top) / 2)
    if(target == alphabet[midpoint]):
        print ("Yay! you found the letter")
        not_found=False
        break
    if(target < alphabet[midpoint]):
        top=midpoint
        print ("left")

    if(target > alphabet[midpoint]):
        bottom=midpoint
        print("right")

if (not_found):
    print ("Sorry, you did not find the letter")
