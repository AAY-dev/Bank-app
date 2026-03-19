file = open("data.txt" , "w")


def createAcount():
    file = open("data.txt" , "a")

    login = input("Login : ")
    password = input("Password : ")

    while (not( validLogin(login) and validPsw(password) )):
        login = input("Login : ")
        password = input("Password : ")

    file.close()

def validLogin(login):
    if ( login.find(" ") != -1 or not( 3 <= len(login) <= 15 )   ):
        return False
    else:
        return True

def validPsw(password):
    if ( not ( 5 <= len(password) <= 12 ) or password.find(" ") != -1 ):
        return False
    else:
        return True

def acountStats():
    pass

def getBalance():
    pass

def deposit(amount):
    pass

def withdraw(amount):
    pass


def main():
    pass