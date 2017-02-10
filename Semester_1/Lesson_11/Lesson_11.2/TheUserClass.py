import random
class User:
   def __init__(self, fName, lName, avat = ""):
       self.firstName = fName
       self.lastName = lName
       self.avatar = avat
       self.userID = random.randint(0, 1000000)

   def setHES(self, newFirstName, newLastName, newAvatar):
      self.firstname = newFirstName
      self.lastname = newLastName
      self.avatar = newAvatar
      self.userID = random.randint(0, 1000000)

   def getFirstName(self):
      return self.firstName

   def getLastName(self):
      return self.lastName

   def getAvatar(self):
      return self.avatar

   def getUserID(self):
      return selfuserID

   def __str__(self):
           print("Customer Info...\nFirst Name: ", self.firstName, "\nLast Name: ", self.lastName, "\nAvatar: ", self.avatar, "\nUser ID#: ", str(self.userID))

def main():
   fName = input("Please enter your first name: ")
   lName = input("Please enter your last name: ")
   avt = input("Would you like to use a public avatar? (y or n)? ")
   if avt == "n":
      user1 = User(fname, lname)
   else:
      avat = input("Please enter your avatar: ")
      user1 = User(fName, lName, avat)

   print(user1.__str__())
      

main()
