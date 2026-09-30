'''
Fractional Knapsack Problem
'''

def fractional_knapsack_allocation(items, capacity):

    items = sorted(items, key=lambda x: (-x[1]/x[2], x[0]))
    result = ["Fractional Knapsack Report", "Selected Items", "Item Value Weight Fraction Profit"]
    total_profit = 0.0
    total_weight = 0.0
    remaining = capacity

    for item_id, value, weight in items:
        if remaining <= 0:
            break
        if weight <= remaining:
            fraction = 1.0
            profit = float(value)
            remaining -= weight
            total_weight += weight
        else:
            fraction = remaining/weight
            profit = value*fraction
            total_weight += remaining
            remaining = 0

        total_profit += profit

        result.append(f"{item_id} {value:.2f} {weight:.2f} {fraction:.2f} {profit:.2f}")
        result.append(f"Maximum Profit: {total_profit:.2f}")
        result.append(f"Total Weight Used: {total_weight:.2f}")
        result.append("Selection Strategy: Highest value-to-weight ratio first")

    return result