try:
    ExpenseName = input("Enter expense name: ")
    ExpenseAmount = int(input("Enter expense amount: "))
    print(f"You spent ${ExpenseAmount:.2f} on {ExpenseName}")
except:  # noqa: E722
    print("Invalid amount! Please enter a number.")
