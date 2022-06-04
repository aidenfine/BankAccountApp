balance = 0
granted = False

valid_option = [1, 2, 3, 4, 5, 9]


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
        tryAgain = int(input("Type '1' to try again \nType '2' to close program"))
        if tryAgain == 1:
            access(option)
        elif tryAgain == 2:
            exit()
        elif tryAgain != 1 or 2:
            print("invalid response now closing... in")
        else:
            print("error")


def register(username, password):
    global balance
    file = open("userInfo/user.txt", "a")
    file.write("\n" + username + "," + password + "," + str(balance))
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
    global nInt
    global n
    global balance
    if granted:
        n = 0
        print("----------------------------------------------------------------")
        print("Welcome", username)
        print("Your balance is: $", balance)
        print(" 1. Deposit \n 2. Send Money \n 3. Check Balance \n 4. USD to crypto \n 5. Foreign \n 9. Log out")
        try:
            n = int(input("Please select one of the options"))
            menu_items()
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Please select a number! ")
            menu_items()


def deposit():
    global balance

    while True:
        try:
            dep = float(input("how much would you like to deposit? $"))
            balance = balance + dep
            print("Your balance is $", round(balance, 2))
            menu(username)
            break
        except ValueError:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("Number only!")

def send_money(username):
    global accept
    global balance
    accept = False
    x = input("Please enter a username to send to: ")
    file = open("userInfo/user.txt", "r")
    for i in file:
        a = i.split(",")
        if a == username:
            accept = True
            try:
                AmtOfMoneyToSend = float(input("How much would you like to send? "))
                if AmtOfMoneyToSend > balance:
                    print("Not enough money \nTry Again!")
                    send_money(username)
                else:
                    AmtOfMoneyToSend = str(AmtOfMoneyToSend)
                    confirm = input("Send $" + AmtOfMoneyToSend + "\n 'y' for yes \n 'n' for no")
                    if confirm == "y":
                        AmtOfMoneyToSend = float(AmtOfMoneyToSend)
                        balance = balance - AmtOfMoneyToSend
                        print("Thank you!")
                        menu(username)
                        break
                    elif confirm == "n":
                        print("Terminating transaction....")
                        menu(username)
                        break
            except ValueError:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Please type in dollar amount")
        elif not accept:
            print("User does not exist!")
            send_money(username)







def check_balance():
    print("Your balance is: $", round(balance, 2))
    menu(username)


def crypto():
    file = open("crypto.py")


def log_out():
    print("----------------------------------------------------------------")
    print("logged out.")
    access(option)


def menu_items():
    global n
    if n == 69:
        menu_items()
    elif n == 1:
        # deposit
        deposit()
    elif n == 2:
        # send money
        send_money(username)
    elif n == 3:
        # check balance
        check_balance()
    elif n == 4:
        # crypto
        crypto()
        pass
    elif n == 5:
        # add foreign later
        pass
    elif n == 9:
        log_out()
    else:
        n = 69
        menu(username)


start()
access(option)
menu(username)
