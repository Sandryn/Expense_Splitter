def calculate_balances(expenses):
    total = sum(expenses.values())
    share = total / len(expenses)
    balances = {name: amount - share for name, amount in expenses.items()}
    return balances
