balance = 1000
print("Welcome to the Atm menu")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Choose an option: "))

if choice == 1:
    print(f'Balance is : {balance}')
elif choice == 2:
    amt = int(input("Enter the amount to deposit : "))
    balance += amt
    print("Deposit successfull")
    print(f"Total balance: {balance}")
elif choice == 3:
    amt = int(input("Enter the amount to withdraw : "))
    if amt<=balance:
        balance -= amt
        print(f"Withdraw {amt} successfull")
        print(f"Remaining balance: {balance}")
    elif amt>balance:
        print("Insufficient balance")
elif choice == 4:
    print("Thank you for using the ATM")
else:
    print("Invalid Option. Try Again")