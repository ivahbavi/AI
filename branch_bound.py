def print_board(board, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += " Q "  # Place queen
            else:
                line += " . "  # Empty space
        print(line)
    print("\n")  # Separate solutions

def is_safe(board, row, col, n):
    # Check for conflicts with queens already placed in previous rows
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def estimate_remaining_queens(board, row, n):
    """
    Estimate if we have enough space to place remaining queens.
    This is a simple implementation that counts available columns in remaining rows.
    """
    # Calculate number of queens we still need to place
    queens_to_place = n - row
    
    # Initialize available spaces in each remaining row
    available_spaces = 0
    
    # For each remaining row
    for i in range(row, n):
        # Count available columns in this row
        available_in_row = 0
        for col in range(n):
            # Only check if this position would be safe from queens in rows 0 to row-1
            if all(board[j] != col and abs(board[j] - col) != abs(j - i) 
                   for j in range(row)):
                available_in_row += 1
        
        # We need at least one available position per row
        if available_in_row == 0:
            return False
        
        available_spaces += available_in_row
    
    # Simple branch bound: we need at least as many spaces as queens to place
    return available_spaces >= queens_to_place

def solve_n_queens_with_branch_bound(board, row, n, solutions):
    # Base case: All queens placed successfully
    if row == n:
        # Copy the solution to our solutions list
        solutions.append(board.copy())
        return
    
    # Branch and bound check: can we place remaining queens?
    if not estimate_remaining_queens(board, row, n):
        return  # Prune this branch
    
    # Try placing a queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # Place queen
            
            # Recur for next row
            solve_n_queens_with_branch_bound(board, row + 1, n, solutions)
            
            # Backtrack
            board[row] = -1

def n_queens(n):
    board = [-1] * n  # Initialize board with -1 (no queen placed)
    solutions = []
    
    # Solve with branch and bound
    solve_n_queens_with_branch_bound(board, 0, n, solutions)
    
    # Print all solutions
    print(f"Found {len(solutions)} solutions for {n}-Queens:")
    for solution in solutions:
        print_board(solution, n)
    
    return solutions

# User input version
def main():
    try:
        n = int(input("Enter the board size (number of queens): "))
        if n <= 0:
            print("Please enter a positive integer.")
            return
        
        # Warn about large board sizes
        if n > 8:
            print("Warning: Large board sizes may take a long time to compute.")
            proceed = input("Do you want to continue? (y/n): ").lower()
            if proceed != 'y':
                return
        
        solutions = n_queens(n)
        print(f"Total number of solutions: {len(solutions)}")
        
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()