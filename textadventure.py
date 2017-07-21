start = '''Its 12am and you hear banging on the door, yelling, then gunshots
everywhere.Loud footsteps come towards your door. You are too shocked to move.
You see your mom, so you get out of bed. She hands you a bookbag, jacket and
shoes then she kisses you and leads you down the stairs and safely out of the
house. She says" run as fast as you can and never look back. One day you'll
learn how to control it." You start running straight into the woods.'''

investigate= '''you turn to the noise and tell the person to show themselves.
Out of the dark, appears your parents! You are releieved; they tell you about
a safe house that ya'll head to. They explain everything to you on the way.'''

run= '''you keep running and eventually find a fork in the path. You can either
 go left or check the bag that your mom gave you. '''

print(start)
done=False
left = False
right= False
while not done:
    print('''5 minutes later you stop to take a break because you're tired.
    Suddenly, you hear a branch snap, you turn around, but nobody is there.
    You can either investigate the noise or continue running''')

    user_input = input()
    if user_input == "run":
        done=True
        print(run)

    elif user_input == "investigate":
        done=True
        print(investigate)

    else:
        print("Wrong Option")
        done=False

print()
check= '''you stop and checked your bag and you find a phone (with inportant contacts),
water,a visa card, $800 in cash, and a key attached to a note that says
 "stay at the safe house until somone contacts you" with an address.
 You can either start heading to the safe house or stop and rest for the night.'''
done=False
while not left:
    user_input = input()
    if user_input== "left":
        done = True
        left = True
        print ('''she goes left and finds a house''')

    elif user_input=="check bag":
        print (check)
