balance = 5000
correct_pin = 1234

pin = int(input("Enter the PIN: "))

if pin == correct_pin:
    print("Access Granted")

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter your deposit amount: "))
        balance += amount
        print("Your new balance:", balance)

    elif choice == 3:
        amount = int(input("Enter your withdrawal amount: "))

        if balance >= amount:
            balance -= amount
            print("Please collect cash")
            print("Your new balance:", balance)
        else:
            print("Insufficient balance")

    elif choice == 4:
        print("Thank you for using ATM")

    else:
        print("Invalid choice")

else:
    print("Invalid PIN")
