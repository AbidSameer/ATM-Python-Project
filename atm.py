import time

users_data = {
    'sameer': 'abid123',
    'saleem': 'saleem123',
    'ismail': 'ismail123',
}

max_attempts = 3
lockout_time = 24 * 60 * 60

def main():
    c_username = input("Enter username: ").lower()

    if c_username in users_data:
        c_password = input("Enter password: ")
        if authenticate(c_username, c_password):
            perform_transaction(c_username)
        else:
            handle_invalid_login(c_username)
    else:
        print("Invalid username")

def authenticate(username, password):
    return users_data.get(username) == password

def perform_transaction(username):
    amount = 50000
    option = 0

    while option != 4:
        print('''
        1. Deposit
        2. Withdraw
        3. Mini Statement
        4. Exit
        ''')
        option = int(input("Select your option: "))

        if option == 1:
            dep = int(input("Enter the amount: "))
            amount += dep
            print("Total amount: ", amount)
        elif option == 2:
            withdraw = int(input("Enter the amount: "))
            amount -= withdraw
            print("Total balance amount: ", amount)
        elif option == 3:
            print("======== ATM ========")
            print("Username:", username)
            print("Total amount:", amount)
            print("Thanks for visiting")
            print("=====================")
        elif option == 4:
            print("Exiting...")
        else:
            print("Invalid option")

def handle_invalid_login(username):
    n = 1
    max_n = 3
    last_attempt_time = time.time()

    while n <= max_n:
        c_password = input("Invalid password. Enter password: ")

        if authenticate(username, c_password):
            print("Login successful.")
            return True
        else:
            print("Invalid password. Please try again.")
            n += 1

    current_time = time.time()
    remaining_time = max(0, last_attempt_time + lockout_time - current_time)

    if remaining_time > 0:
        print(f"Too many failed attempts. Try again after {format_time(remaining_time)}")
        warn_if_before_lockout(username, last_attempt_time, lockout_time)
    else:
        print("Please try after 24 hours")

    return False

def warn_if_before_lockout(username, last_attempt_time, lockout_time):
    current_time = time.time()
    time_until_lockout = max(0, last_attempt_time + lockout_time - current_time)

    if time_until_lockout > 0:
        print(f"Warning: Attempting login before 24 hours may result in lockout.")
        print(f"Remaining time until lockout: {format_time(time_until_lockout)}")

    c_username = input("Enter username again: ").lower()

    if c_username == username:
        print(f"Warning: Attempting login with the same username before 24 hours may result in lockout.")
        print(f"Remaining time until lockout: {format_time(time_until_lockout)}")
        main()  

def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

if __name__ == "__main__":
    main()


        
        
    

    
