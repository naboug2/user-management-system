
Email = input("Enter your email address:  ")
Password = input("Enter your password:  ")

FileLocation = "C:\\Users\\ashulm2\\Downloads\\UIN and NetID\\"
UsersFile = open(FileLocation + "users.txt","r")
Users = UsersFile.read()
UsersFile.close()
Users = Users.split("\n")
N = len(Users)

EmailFound = False
for i in range(N):
  if Users[i] == Email:
    EmailFound = True
    if Users[i+1] == Password:
      print("You have successfully logged in!")
    else:
      print("That password does not match the email provided.")

if EmailFound == False:
  print("That email is not in our system")