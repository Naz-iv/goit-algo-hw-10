from pulp import (
    LpProblem,
    LpMaximize,
    LpVariable,
    PULP_CBC_CMD,
    LpStatus,
    value
)


def main():
    model = LpProblem("Maximize_Production", LpMaximize)

    x1 = LpVariable("Lemonade", lowBound=0, cat="Integer")
    x2 = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    model += x1 + x2, "Total_Profit"

    water_limit = 2 * x1 + x2 <= 100
    sugar_limit = x1 <= 50
    lemon_juice_limit = x1 <= 30
    fruit_puree_limit = 2 * x2 <= 40

    model += water_limit, "Water_Constraint"
    model += sugar_limit, "Sugar_Constraint"
    model += lemon_juice_limit, "Lemon_Juice_Constraint"
    model += fruit_puree_limit, "Fruit_Puree_Constraint"

    model.solve(PULP_CBC_CMD(msg=0))

    print("Status:", LpStatus[model.status])
    print(f"{LpStatus[model.status]} Production Quantity:")
    print(f"Lemonade: {value(x1):.0f}")
    print(f"Fruit Juice: {value(x2):.0f}")
    print(f"Maximum Production: {value(model.objective):.0f}")


if __name__ == "__main__":
    main()
