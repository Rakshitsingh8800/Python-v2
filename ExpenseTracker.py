# Expense Tracker: Kharcha kam kiya karo laadlo!

expenses = [] # list of expenses in form of dictionaries

print("Welcome to the Expense Tracker: Kharcha kam kiya karo laadlo!")

while True:
    print("======MENU======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = (int(input("Enter your choice (1-4): ")))
# Add Expense
    if (choice == 1):
        date = input("Enter the date (YYYY-MM-DD): ")
        category = input("Enter the category (e.g., Food, Transport): ")
        description = input("Enter a description: ")
        amount = float(input("Enter the amount: "))

        expense = {
            'date': date,
            'category': category,
            'description': description,
            'amount': amount
        }

        expenses.append(expense)
        print("\n Expense added successfully!")

# View Expenses
    elif (choice == 2):
        if(len(expenses) == 0):
            print("\n No expenses added yet.")
        else:
            print("\n ======Your Expenses======")
            for each in expenses:
                print(f"Date: {each['date']}, Category: {each['category']}, Description: {each['description']}, Amount: {each['amount']}")

# View Total Expense
    elif (choice == 3):
        total = 0
        for each in expenses:
            total += each['amount']
        print(f"\n Total Expense: {total}")

# Exit
    elif (choice == 4):
        print("\n Thank you for using the Expense Tracker. Goodbye! | Made by: Rakshit Singh | with ❤️")
        break
    else:
        print("\n Invalid choice. Please enter a number between 1 and 4.")