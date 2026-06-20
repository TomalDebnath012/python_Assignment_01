# Problem 19
# Create a simple login system using nested if-else.
correct_username="admin"
correct_password="1234"
username=input("Enter username: ")
password=input("Enter password: ")
if username==correct_username:
    if password==correct_password:
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("User Not Found")