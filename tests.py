from computation import calculate_balances

def test_balances():
    expenses = {"A": 100, "B": 200, "C": 100}
    result = calculate_balances(expenses)
    assert abs(sum(result.values())) < 0.01  # total balances should cancel out
