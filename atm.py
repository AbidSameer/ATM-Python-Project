
username='sameer'
password='abid123'

c_username=input("Enter username ")
c_password=input("Enter password ")

if(c_username==username and c_password==password):
    print('''
    1.deposit
    2.withdraw
    3.ministatement
    4.exit
    ''')
    amount=50000
    option=int(input("Select your option: "))
    if (option==1):
        dep=int(input("Enter the amount"))
        amount=amount+dep
        print("Total amount ",amount)
    elif (option==2):
        withdraw=int(input("Enter the amount "))
        amount=amount-withdraw
        print("Total  balance amount ",amount)
    elif (option==3):
        print("========ATM=========")
        print("Username:",username)
        print("Total amount:",amount)
        print("Thanks for visiting")
        print("===================")
    elif (option==4):
        exit()
    else:
        print("Please enter correct logins")
    
