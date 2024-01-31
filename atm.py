import time
username='sameer'
password='abid123'
c_username=input("Enter username ")
c_password=input("Enter password ")
n=1
max_n=3
time=24*60*60
while(password!=c_password and n<max_n):
    print("please try again")
    c_password=input("Enter password ")
    n+=1
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
else:
    print("Please try after 24 hours")
    for i in range(time,0,-1):
        hours, remainder = divmod(i, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_format = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)
        print(f"Next attempt available in {time_format}", end="\r")

        
        
    

    
