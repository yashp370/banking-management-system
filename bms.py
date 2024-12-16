# banking management system

import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='yp'  
)
cursor = db.cursor()

def create_account(account_number, name, phone, initial_deposit):
    cursor.execute("INSERT INTO customers (Account_Number, Account_Name, Phone_Number, Balance) VALUES (%s, %s, %s, %s)", 
                   (account_number, name, phone, initial_deposit))
    db.commit()
    print(f"Account created successfully. Account Number: {account_number}")

def view_account(account_number):
    cursor.execute("SELECT * FROM customers WHERE Account_Number = %s", (account_number,))
    account = cursor.fetchone()
    if account:
        print("ID:", account[0])
        print("Account Number:", account[1])
        print("Name:", account[2])
        print("Phone Number:", account[3])
        print("Balance:", account[4])
    else:
        print("Account not found.")

def deposit_money(account_number, amount):
    
    cursor.execute("SELECT * FROM customers WHERE Account_Number = %s", (account_number,))
    account = cursor.fetchone()
    
    if account is None:
        print("This account does not exist or is not found.")
        return
    

    cursor.execute("UPDATE customers SET Balance = Balance + %s WHERE Account_Number = %s", (amount, account_number))
    db.commit()
    print("Deposit successful.")
   

def withdraw_money(account_number, amount):
    cursor.execute("SELECT Balance FROM customers WHERE Account_Number = %s", (account_number,))
    result = cursor.fetchone()
    
    if result is None:
        print("Account not found.")
        return
    
    balance = result[0]
  

    if balance is None:
        print("Account has no balance.")
        return
    
    if balance >= amount:
        cursor.execute("UPDATE customers SET Balance = Balance - %s WHERE Account_Number = %s", (amount, account_number))
        db.commit()
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

def delete_account(account_number):
    cursor.execute("DELETE FROM customers WHERE Account_Number = %s", (account_number,))
    db.commit()
    print("Account deleted successfully.")


def login():
    print("\n--- Login ---\n")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "admin@123":
        return "admin"
    elif username == "customer" and password == "cus@123":
        return "customer"
    else:
        print("Invalid credentials! Try again.")
        return None

def admin_menu():
    while True:
        print("\n-----------Banking Management System----------")
        print("\n  Welcome \n")
        print("\n1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            account_number = int(input("Enter the account number: "))
            name = input("Enter account holder's name: ")
            phone = input("Enter phone number: ")
            initial_deposit = float(input("Enter initial deposit amount: "))
            create_account(account_number, name, phone, initial_deposit)

        elif choice == '2':
            account_number = int(input("Enter Account Number: "))
            view_account(account_number)

        elif choice == '3':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter amount to deposit: "))
            deposit_money(account_number, amount)

        elif choice == '4':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(account_number, amount)

        elif choice == '5':
            account_number = int(input("Enter Account Number: "))
            delete_account(account_number)

        elif choice == '6':
            print("Exiting the program.")
            print("Thank you for using the BMS. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def customer_menu():
    while True:
        print("-----------Banking Management System----------")
        print("\n  Welcome \n")
        print("1. View Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            account_number = int(input("Enter Account Number: "))
            view_account(account_number)



        elif choice == '2':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter amount to deposit: "))
            deposit_money(account_number, amount)

        elif choice == '3':
            account_number = int(input("Enter Account Number: "))
            amount = float(input("Enter amount to withdraw: "))
            withdraw_money(account_number, amount)



        elif choice == '4':
            print("Exiting the program.")
            print("Thank you for using the BMS. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



def main_menu():
    role = login()
    if role == "admin":
        admin_menu()
    elif role == "customer":
        customer_menu()
    else:
        print("Login failed. Exiting system.")
        exit()
        

main_menu()
cursor.close()
db.close()



