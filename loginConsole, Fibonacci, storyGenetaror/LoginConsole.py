class accountData:

    def __init__(self, firstName, lastName, email, password):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

def authentication(auth):

    askAuth = input("Please provide your ID for authentication\n")

    existingUsers = ["dmichalc"]

    for id in existingUsers:
        if(askAuth) in existingUsers:
            authenticated = True
        else:
            authenticated = False
    
    return authenticated

askBreak = input("Something")

#Here will be check if user exists in file

print("Welcome to the system.. You have not account yet, you need to register")


askForFirstName = input("Please provide your first name")