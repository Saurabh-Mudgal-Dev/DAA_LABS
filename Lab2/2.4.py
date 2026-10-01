'''
0/1 knapsack problem using Dynamic Programming
'''

def knapsack_comparison(items, capacity):

  n = len(items)
  dp = [[0]*(capacity+1) for _ in range(n+1)]
  for i in range(1, n+1):
    _, value, weight = items[i-1]
    for w in range(capacity+1):
      if weight <= w:
        dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
      else:
        dp[i][w] = dp[i-1][w]
  selected = []
  w = capacity
  for i in range(n, 0, -1):
    if dp[i][w] != dp[i-1][w]:
      selected.append(i-1)
      w -= items[i-1][2]
  selected.reverse()

  zero_one_value = dp[n][capacity]
  zero_one_weight = sum(items[i][2] for i in selected)

  frac_items = sorted(items, key=lambda x: (-x[1]/x[2], x[0]))
  
  remaining = capacity
  frac_selected = []
  total_weight = 0.0
  total_profit = 0.0

  for item_id, value, weight in frac_items:
    if remaining == 0:
      break
    if weight <= remaining:
      fraction = 1.0
      profit = float(value)
      taken_weight = float(weight)
    else:
      fraction = remaining / weight
      profit = value * fraction
      taken_weight = float(remaining)
    frac_selected.append((item_id, float(value), float(weight), fraction, profit))

    total_profit += profit
    total_weight += taken_weight
    remaining -= taken_weight

  diff = total_profit-zero_one_value
  lines = []
  lines.append("Knapsack Comparison Report")
  lines.append("0/1 Knapsack")
  lines.append("Selected Items")
  lines.append("Item Value Weight")
  for i in selected:
    item_id, value, weight = items[i]
    lines.append(f"{item_id} {value} {weight}")
  lines.append(f"Maximum Value: {zero_one_value}")
  lines.append(f"Total Weight: {zero_one_weight}")

  lines.append("Fractional Knapsack")
  lines.append("Selected Items")
  lines.append("Item Value Weight Fraction Profit")
  for item_id, value, weight, fraction, profit in frac_selected:
    lines.append(f"{item_id} {value:.2f} {weight:.2f} {fraction:.2f} {profit:.2f}")
  lines.append(f"Maximum Profit: {total_profit:.2f}")
  lines.append(f"Total Weight: {total_weight:.2f}")
  lines.append("Comparison")
  lines.append(f"Difference: {diff:.2f}")

  if total_profit > zero_one_value:
    better = "Fractional Knapsack"
  elif total_profit < zero_one_value:
    better = "0/1 Knapsack"
  else:
    better = "Both Equal"
  lines.append(f"Better Result: {better}")
  lines.append("Justification: Fractional Knapsack can take item fractions, while 0/1 Knapsack selects complete items only")
  
      
  return lines