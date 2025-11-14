import os
import json


def load_data():
    if os.path.exists("atm.json"):
        try:
            with open("atm.json", "r") as file:
                data = json.load(file)
                if not isinstance(data, dict):
                    return {
                        "1111222233334444": {
                            "id": "1111222233334444",
                            "balance": 16351,
                            "name": "Bekhzod Turdaliyev",
                            "password": "17501750"
                        }
                    }
                return data
        except json.JSONDecodeError:
            return {
                "1111222233334444": {
                    "id": "1111222233334444",
                    "balance": 16351,
                    "name": "Bekhzod Turdaliyev",
                    "password": "17501750"
                }
            }
    else:
        return {
            "1111222233334444": {
                "id": "1111222233334444",
                "balance": 16351,
                "name": "Bekhzod Turdaliyev",
                "password": "17501750"
            }
        }


def save_data(atm):
    with open("atm.json", "w") as file:
        json.dump(atm, file, indent=4)

def add_user(atm: dict):
    while True:
        user_id = input("enter ID (16 digits): ")
        if len(user_id) == 16:
            break
        else:
            print("invalid request")
    
    if user_id in atm:
        print("this ID already exists")
        return
    user_balance = float(input("enter initial balance(usd): "))
    user_name = input("enter your full name: ")
    password = input("set password: ")
    
    new_user = {
        "id":user_id,
        "balance":user_balance,
        "name": user_name,
        "password": password
    }
    atm[user_id]=new_user
    save_data(atm)
    print("new user added successfully")
    
def manage_account(atm: dict):
    user_selection = input("Enter your ID: ")
    if user_selection not in atm:
        print("card not found")
        return
    while True:
        password = input("Enter password: ")
        if password == atm[user_selection]['password']:
            print("Correct password")
            break
        else:
            print("access denied")
            access = input("would you like to leave this account? \n 1. yes \n 2. no \n choose(1,2): ")
            if access == "1":
                main()
            elif access == "2":
                continue
            else:
                print("invalid request. Exiting account...")
                main()
                
                
    while True:
        user = atm[user_selection]
        balance = float(user["balance"])
        print(f"\nWelcome, {user['name']}!")
        print(f"Your current balance: ${balance:.2f}")
        action = input("1. replenish account \n 2. withdraw balance \n 3. exit \n Choose action: ")
    
        if action == "1":
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            user["balance"] = balance
            print(f"Balance updated: ${balance:.2f}")

        elif action == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                user["balance"] = balance
                print(f"Balance updated: ${balance:.2f}")
            else:
                print("Error: Insufficient funds.")

        elif action == "3":
            print("Exiting account...")
            break
        else:
            print("Invalid request, try again.")
        save_data(atm)
        
def main():
    atm = load_data()
    while True:
        print("\n=== ATM MENU ===")
        print("1. Add new user")
        print("2. Manage existing account")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_user(atm)
        elif choice == "2":
            manage_account(atm)
        elif choice == "3":
            save_data(atm)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
        
main()
            
            
        

    
