def solve(meal_cost, tip_percent, tax_percent):
    print(
        round(
            meal_cost + meal_cost * tip_percent * 0.01 + meal_cost * tax_percent * 0.01
        )
    )


if __name__ == "__main__":
    # meal_cost = float(input())

    # tip_percent = int(input())

    # tax_percent = int(input())

    meal_cost = 12.00
    tip_percent = 20
    tax_percent = 8

    solve(meal_cost, tip_percent, tax_percent)
