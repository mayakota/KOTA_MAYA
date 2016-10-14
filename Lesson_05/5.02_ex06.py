def recursion():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")


    if username == "username" and password == "password":
        print("correct.")


    else:
        if password == "password":
            print("Username is incorrect.")
            recursion()
        elif username == "username":
            print("Password is incorrect.")
            recursion()

        else:
            print("Username and password are incorrect.")
            recursion()
            



recursion()

