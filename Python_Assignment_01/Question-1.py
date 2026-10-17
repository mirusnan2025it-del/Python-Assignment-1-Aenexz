username = input("Enter your username: ")

if username.strip() == "":
    print("Invalid username: Username cannot contain only spaces.")
elif len(username) < 5:
    print("Invalid username: Username must contain at least 5 characters.")
elif username.lower() == "admin":
    print("Invalid username: 'admin' is not allowed.")
else:
    print("Valid username!")
