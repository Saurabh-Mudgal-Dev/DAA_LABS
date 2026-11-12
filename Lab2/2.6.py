'''
Longest common subsequence
'''

def solve(s1, s2):
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = "".join(reversed(lcs))
    if not lcs:
        lcs = "None"

    return [
        "LCS Analysis Report",
        f"LCS Length: {dp[m][n]}",
        f"LCS String: {lcs}",
        f"DP Table Size: {(m + 1)} x {(n + 1)}",
        f"DP Cell Computations: {m * n}",
        "Time Complexity: O(m*n)",
        "Space Complexity: O(m*n)"
    ]