# Define a list to store expenses as dictionaries
expenses = []

# Function to add an expense
def add_expense(item, cost):
    expense = {"Item": item, "Cost": cost}
    expenses.append(expense)
    print(f"Expense for '{item}' has been added: ${cost:.2f}\n")

# Function to list all expenses
def list_expenses():
    if not expenses:
        print("No expenses to display.")
    else:
        total = sum(expense["Cost"] for expense in expenses)
        print("Expenses:")
        for expense in expenses:
            print(f"Item: {expense['Item']}, Cost: ${expense['Cost']:.2f}") #2f means to round up to two decimal places. for example 38.2000
        print(f"Total expenses: ${total:.2f}\n")

# Main program
if __name__ == "__main__":
    print("Welcome to the Expense Tracker!\n")

    while True:
        print("Options:")
        print("1. Add an expense")
        print("2. List all expenses")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            item = input("Enter the item name: ")
            try:
                cost = float(input("Enter the cost in dollars: "))
                if cost >= 0:
                    add_expense(item, cost)
                else:
                    print("Cost must be a non-negative number.\n")
            except ValueError:
                print("Invalid input. Please enter a valid cost as a number.\n")
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")
