# ///////////////////////////////////////////////
# mini banking System




accounts = {}

while True:
    print("\n--- Mini Banking System ---")
    print("1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transfer money")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            print("Account already exists!")
        else:
            accounts[acc_no] = 0
            print("Account created successfully!")

    elif choice == 2:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter deposit amount: "))
            accounts[acc_no] += amount
            print("Deposit successful!")
        else:
            print("Account not found.")

    elif choice == 3:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter withdrawal amount: "))
            if accounts[acc_no] >= amount:
                accounts[acc_no] -= amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    elif choice == 4:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            print(f"Balance: {accounts[acc_no]}")
        else:
            print("Account not found.")

    elif choice == 5:
        sender = input("Enter sender account number: ")
        receiver = input("Enter receiver account number: ")
        amount = int(input("Enter transfer amount: "))
        if sender in accounts and receiver in accounts:
            if accounts[sender] >= amount:
                accounts[sender] -= amount
                accounts[receiver] += amount
                print("Transfer successful!")
            else:
                print("Insufficient balance in sender account.")
        else:
            print("Invalid account number(s).")

    elif choice == 6:
        print("Exiting system...")
        break

    else:
        print("Invalid choice! Try again.")
