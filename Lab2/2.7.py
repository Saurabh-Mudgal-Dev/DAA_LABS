'''
Optimization technique Reflection Report
'''

def solve(n, scenarios):
    ans = [
        "Optimization Technique Reflection Report",
        "Technique Comparison:",
        "Divide-and-Conquer: Breaks a problem into smaller subproblems, solves them recursively, and combines the results.",
        "Greedy: Makes the locally optimal choice at each step to achieve a global solution when applicable.",
        "Dynamic Programming: Solves overlapping subproblems by storing intermediate results to avoid recomputation.",
        "Scenario-wise Recommendations:"
    ]

    mapping = {
        "TASK_SORTING": (
            "Divide-and-Conquer",
            "Sorting can be efficiently solved by recursively dividing and merging."
        ),
        "MEETING_SCHEDULE": (
            "Greedy",
            "Selecting meetings by earliest finish time gives an optimal schedule."
        ),
        "RESOURCE_FRACTION": (
            "Greedy",
            "Choosing the highest value-to-weight ratio first gives the optimal solution."
        ),
        "JOB_PROFIT": (
            "Greedy",
            "Scheduling the most profitable jobs first maximizes profit."
        ),
        "ZERO_ONE_KNAPSACK": (
            "Dynamic Programming",
            "Overlapping subproblems require storing intermediate results."
        ),
        "SEQUENCE_MATCHING": (
            "Dynamic Programming",
            "LCS involves overlapping subproblems solved efficiently using DP."
        )
    }

    for code in scenarios:
        tech, reason = mapping[code]
        ans.append(f"{code}: {tech} - {reason}")

    ans.append("Summary:")
    ans.append("Divide-and-Conquer is suitable for recursive decomposition problems.")
    ans.append("Greedy is suitable when local optimal choices lead to a global optimum.")
    ans.append("Dynamic Programming is suitable for problems with overlapping subproblems and optimal substructure.")
    ans.append("Conclusion: Choose the algorithm design technique based on the structure and properties of the problem.")

    return ans