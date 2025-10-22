def show_results(balances):
    print("Expense Balances:")
    for name, balance in balances.items():
        status = "owes" if balance < 0 else "is owed"
        print(f"{name} {status} {abs(balance):.2f} UGX")
