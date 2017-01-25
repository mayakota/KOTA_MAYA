import random
class User:
   def __init__(self, fName, lName, avat = ""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 1000000)

       user1 = User(first, last)
       print(user1)
       def __str__(self):
           return "Customer Info...\nFirst Name: " + self.firstName + \
                           "\nLast Name: " + self.lastName + \
                           "\nAvatar: " + self.avatar + \
                           "\nUser ID#: " + str(self.userID)


