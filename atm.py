
class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def authenticate(self, pin):
        return self.pin == pin

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def check_balance(self):
        return self.balance

class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, pin):
        if account_number in self.accounts:
            print("Account already exists")
        else:
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully")

    def access_account(self, account_number, pin):
        if account_number not in self.accounts:
            print("Account not found")
        elif not self.accounts[account_number].authenticate(pin):
            print("Invalid PIN")
        else:
            return self.accounts[account_number]
        return None

def main():
    banking_system = BankingSystem()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            banking_system.create_account(account_number, pin)
        elif choice == "2":
            account_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            account = banking_system.access_account(account_number, pin)

            if account:
                while True:
                    print("\nAccount Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Exit")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        try:
                            amount = float(input("Enter amount to deposit: $"))
                            account.deposit(amount)
                            print(f"Deposit successful. New balance: ${account.check_balance():.2f}")
                        except ValueError:
                            print("Invalid input. Please enter a valid amount.")
                    elif choice == "2":
                        try:
                            amount = float(input("Enter amount to withdraw: $"))
                            account.withdraw(amount)
                            print(f"Withdrawal successful. New balance: ${account.check_balance():.2f}")
                        except ValueError as e:
                            print(e)
                    elif choice == "3":
                        print(f"Current balance: ${account.check_balance():.2f}")
                    elif choice == "4":
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
     main()
