from data_input import get_expenses
from computation import calculate_balances
from display import show_results

if __name__ == "__main__":
    expenses = get_expenses()
    balances = calculate_balances(expenses)
    show_results(balances)
