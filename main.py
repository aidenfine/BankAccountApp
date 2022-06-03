balance = 0
granted = False


# gives access
def grant():
    global granted
    granted = True


# login system
def login(username, password):
    global balance
    valid = False
    file = open("userInfo/user.txt", "r")
    for i in file:
        a, b, c = i.split(",")
        b = b.strip()
        if a == username and b == password:
            valid = True
            balance = int(input("What is your balance: "))
            break
    file.close()
    if valid:
        print("Login Successful.")
        grant()
    else:
        print("Wrong username or password")


def register(username, password):
    global balance
    file = open("userInfo/user.txt", "a")
    file.write("\n" + username + "," + password + "," + balance)
    file.close()
    print("You have been registered ")
    grant()


def access(option):
    global username
    global balance
    if option == "login":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username, password)
    else:
        print("Please create a username and password. ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        balance = int(input("You need a starting deposit please enter it now: "))
        register(username, password)


def start():
    global option
    print("Welcome to the basic bank account! ")
    option = input("Login or Register (login,reg): ")
    if option != "login" and option != "reg":
        start()


# main program
def menu(username):
    global n
    global balance
    if granted:
        n = 0
        print("Welcome", username)
        print(" 1. Deposit \n 2. Withdraw \n 3. Check Balance \n 4. USD to crypto \n 5. Foreign \n 9. Log out")
        n = int(input("Please select one of the options"))
        menu_items()


def deposit():
    global balance
    dep = float(input("how much would you like to deposit? "))
    balance = balance + dep
    print("Your balance is $", round(balance, 2))
    menu(username)


def withdraw():
    pass


def check_balance():
    print("Your balance is: ", round(balance, 2))




def menu_items():
    global n
    if n == 1:
        deposit()
    elif n == 2:
        withdraw()
    elif n == 3:
        check_balance()
    elif n == 4:
        # add crypto
        pass
    elif n == 5:
        # add foreign later
        pass
    elif n == 9:
        # log out
        pass
    else:
        menu_items()

start()
access(option)
menu(username)



