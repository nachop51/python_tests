from getpass import getpass

def password():
    password = getpass("Enter a password:\n> ")
    confirmPassword = getpass("Confirm your password:\n> ")
    if password == confirmPassword:
        print("Perfect!")
    else:
        print("The passwords do not match")

password()