money = 1000
interest_rate = 1.15
n = 5

after_five_years = (money * interest_rate ** n) - 500


def after_five_years(n):
    (money * interest_rate ** n) - 500


after_ten_years = after_five_years(10)

print(after_ten_years)
