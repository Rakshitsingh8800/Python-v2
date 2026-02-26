class BankAccount:

    # constructor
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        print(f"\nAccount created for {self.account_holder}")

        # Deposit method
    def deposit(self , amount):
            if amount > 0:
                self.balance  += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")

            # Withdraw method
    def withdraw(self, amount):
                if amount > self.balance:
                    print("Insufficient balance.")
                elif amount <= 0:
                    print("Invalid withdrawal amount.")
                else:
                    self.balance -= amount
                    print(f"₹{amount} withdrawn successfullly.")

    def display(self):
                    print("\n----Account Details----")
                    print("Account Holder: ", self.account_holder)
                    print("Account Number: ", self.account_number)
                    print("Balance: ₹", self.balance)

                    # Destructor
    def __del__(self):
          print(f"\nAccount of {self.account_holder} is closed.")

 #   Creaing objects
acc1 = BankAccount("Rahul", 101, 5000)
acc2 = BankAccount("Anita", 102, 10000)

# Using methods
acc1.deposit(2000)
acc1.withdraw(1500)
acc1.display()

acc2.deposit(12000)
acc2.withdraw(3000)
acc2.display()

# Deleting object

del acc1
del acc2