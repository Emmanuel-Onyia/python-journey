user = input("Please enter your username: ")
passwd = input("Please enter your secret code: ")

if passwd == "admin123":
    print("Username:", user)
    print("Password:", passwd)
    print("Login successful")
else:
    print("Username:", user)
    print("Password:", passwd)
    print("Login failed. Access denied")

