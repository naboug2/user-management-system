import random

def PasswordGenerator():
  """this function will generate a random password of upper and lower case vowels of length between 4 and 8; the password will not contain any of the same vowels adjacent to one another (either upper or lower case)"""
  n = random.randint(4,8) #choose the length of the password
  Vowels = "AEIOUaeiou"
  P = random.choice(Vowels) #initially choose a vowel to start the password
  while len(P) < n: #loop until the length of the password is n characters long
    Next = random.choice(Vowels)
    if Next.lower() != P[-1].lower(): #if the next vowel does not match the previous vowel (converting them to lowercase for comparison), then add it to the password
      P += Next
  return P

FileLocation = "C:\\Users\\ashulm2\\Downloads\\UIN and NetID\\"
UINFile = open(FileLocation + "UIN.txt","r")
UINContents = UINFile.read().strip() #strip removes and blank lines
UINFile.close()
NetIDFile = open(FileLocation + "NetID.txt","r")
NetIDContents = NetIDFile.read().strip()
NetIDFile.close()
UIN = UINContents.split("\n")
NetID = NetIDContents.split("\n")

AllUsers = {}
for i in range(len(UIN)):
  if UIN[i] not in AllUsers:
    NewUIN = str(UIN[i]).zfill(7) #fill in 0's until string is 7 characters long
    AllUsers[NewUIN] = {
      "email": NetID[i] + "@uic.edu",
      "password": PasswordGenerator()
    }

UsersFile = open(FileLocation + "users.txt","w")
for u in AllUsers:
  UsersFile.write(AllUsers[u]["email"] + "\n")
  UsersFile.write(AllUsers[u]["password"] + "\n")

UsersFile.close()




    