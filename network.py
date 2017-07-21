class User:
    # Define the fields and methods for your object here.
    def __init__ (self, newUsername, newUserID):
        self.username = newUsername
        self.userID = newUserID
        self.friends = []

    def getUsername(self):
        return self.username

    def getUserID(self):
        return self.userID

    def getFriends(self):
        return self.friends

    def addFriends(self, friendID):
        self.friends.append(friendID)

class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users=[]

    def numUsers(self):
        return len(self.users)

    def addUser(self, username):
        user_id=len (self.users)
        self.users.append(User(username,user_id))

    def getUserID(self, username):
        for user in self.users:
            if username==user.getUsername():
                user_id=user.getUserID()
        return user_id

    def addConnection(self,user1,user2):
        user1_id=self.getUserID(user1)
        user2_id=self.getUserID(user2)

        user1=self.users[user1_id]
        user2=self.users[user2_id]

        self.users[user2_id].addFriends(user1_id)
        self.users[user1_id].addFriends(user2_id)

    def printUsers(self):
        print("This is the Network")
        for user in self.users:
            print ("\tUser {}: {}".format(user.getUserID( ), user.getUsername()))


    def printConnections(self,username):
        user=self.users[self.getUserID(username)]
        connections=user.getFriends()
        print("\t{}'s connections".format(user.getUsername()))
        for friendID in connections:
            friend=self.users[friendID]
            print("\t{}".format(friend.getUsername()))


def main():
    # Define the program flow for your user interface here.
    mynetwork=Network()
    done=False
    while not done:
        action=input ("\nWhat would you like to do? Add a user(u), Add a Connection (c) Print Users (p), Print Connection(pc), Exit(e)")

        if action=="u":
            username=input("What username?")
            mynetwork.addUser(username)
        elif action=="c":
            if mynetwork.numUsers()<2:
                print("ERROR.Don't have enough users.")
                continue
            else:
                user1=input("First User?")
                user2=input("Second User?")
            mynetwork.addConnection(user1,user2)

        elif action=="p":
            mynetwork.printUsers()

        elif action=="pc":
            user=input("What User?")
            mynetwork.printConnections(user)

        elif action=="e":
            print("K. Byeee :)")
            done=True
        else:
            print ("ERROR. What r u doin? you need to enter a letter")

    #Menu for the user to select through
# Runs your program.
if __name__ == '__main__':
    main()
