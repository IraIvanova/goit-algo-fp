def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    result = {}

    for item in sorted_items:
        if item[1]["cost"] <= budget:
            result[item[0]] = item[1]
            budget -= item[1]["cost"]

    return {
        "total_calories": sum(item["calories"] for item in result.values()),
        "items": result
    }


def dynamic_programming(items, budget):
    amount = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    for item_name, item_data in items.items():
        cost = item_data["cost"]
        calories = item_data["calories"]

        for current_budget in range(budget, cost - 1, -1):
            previous_budget = current_budget - cost
            new_calories = amount[previous_budget] + calories

            if new_calories > amount[current_budget]:
                amount[current_budget] = new_calories
                selected_items[current_budget] = selected_items[previous_budget] + [{item_name: item_data}]

    return {
        "total_calories": amount[budget],
        "items": selected_items[budget]
    }


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 75

    print("Greedy Algorithm: ")
    print(greedy_algorithm(items, budget))

    print("\nDynamic Programming: ")
    print(dynamic_programming(items, budget))
