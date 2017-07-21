my_list = ["cookies", "shampoo", "paint", "cashews", "water", "books"]
main_courses= ["chicken_alfredo","salmon", "enchilada", "meatloaf", "pot_roast"]
desserts= ["ice_cream", "brownie", "creme_brule", "cheesecake", "apple_pie"]


def OnList(groceries):
    for item in groceries:
        print (item)


OnList(my_list)
print("------------------------")

OnList(desserts)
print ('----------------------')

OnList(main_courses)
print ("-----------------------")
