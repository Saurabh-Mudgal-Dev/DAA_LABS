'''
N-Queens problem
'''

def solve(n):
    board = [["."] * n for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()
    positions = []

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            positions.append((row, col))

            if backtrack(row + 1):
                return True

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            positions.pop()
        return False

    found = backtrack(0)

    ans = ["N Queens Backtracking Report"]
    ans.append(f"Board Size: {n}")
    ans.append(f"Solution Found: {'Yes' if found else 'No'}")

    if found:
        ans.append("Board:")
        for row in board:
            ans.append(" ".join(row))
        ans.append("Queen Positions:")
        for r, c in positions:
            ans.append(f"({r}, {c})")
    else:
        ans.append("No solution is possible.")

    ans.append("Time Complexity: O(N!)")
    ans.append("Space Complexity: O(N)")
    ans.append("Observation: Backtracking explores valid placements row by row and backtracks whenever a conflict occurs.")

    return ans