class PuzzleState:
    def __init__(self, board, parent=None, move=None):
        self.board = board
        self.parent = parent
        self.move = move
        if parent is None:
            self.g = 0
        else:
            self.g = parent.g + 1
        self.h = self.calculate_manhattan_distance()
        self.f = self.g + self.h

    def calculate_manhattan_distance(self):
        """Manhattan Distance = sum of absolute differences between current and goal positions"""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_row = (value - 1) // 3
                    goal_col = (value - 1) % 3
                    distance = distance + abs(i - goal_row) + abs(j - goal_col)
        return distance

    def get_blank_position(self):
        """Find the position of the blank tile (represented by 0)"""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def get_possible_moves(self):
        """Return a list of new PuzzleState objects for valid moves"""
        moves = []
        pos = self.get_blank_position()
        x = pos[0]
        y = pos[1]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for d in directions:
            dx = d[0]
            dy = d[1]
            new_x = x + dx
            new_y = y + dy

            if new_x >= 0 and new_x < 3 and new_y >= 0 and new_y < 3:
                # Create a copy of the board manually
                new_board = []
                for row in self.board:
                    new_row = []
                    for item in row:
                        new_row.append(item)
                    new_board.append(new_row)

                # Swap blank with target tile
                temp = new_board[new_x][new_y]
                new_board[new_x][new_y] = new_board[x][y]
                new_board[x][y] = temp

                moves.append(PuzzleState(new_board, self, (new_x, new_y)))
        return moves

def boards_equal(board1, board2):
    """Check if two boards are equal manually"""
    for i in range(3):
        for j in range(3):
            if board1[i][j] != board2[i][j]:
                return False
    return True

def board_in_list(board, board_list):
    """Check if a board is already in the list of visited boards"""
    for b in board_list:
        if boards_equal(board, b):
            return True
    return False

def get_solution_path(state):
    """Return the path from the initial state to the goal state"""
    path = []
    while state is not None:
        path.insert(0, state.board)  # Insert at beginning (no slicing used)
        state = state.parent
    return path

def print_board(board):
    """Print a single 3x3 puzzle board"""
    for i in range(3):
        row = board[i]
        print(row[0], row[1], row[2])
    print()

def solve_puzzle(initial_board):
    """A* Search algorithm for solving the 8-puzzle"""
    start_state = PuzzleState(initial_board)
    open_list = [start_state]
    closed_list = []

    while len(open_list) > 0:
        # Find state with the smallest f value manually
        min_f_index = 0
        for i in range(1, len(open_list)):
            if open_list[i].f < open_list[min_f_index].f:
                min_f_index = i

        current = open_list[min_f_index]
        open_list.pop(min_f_index)

        if current.h == 0:
            return get_solution_path(current)

        if board_in_list(current.board, closed_list):
            continue

        closed_list.append(current.board)

        neighbors = current.get_possible_moves()
        for i in range(len(neighbors)):
            open_list.append(neighbors[i])

    return None

def main():
    # Initial 8-puzzle state (0 represents blank)
    initial_board = [
        [1, 2, 3],
        [4, 5, 6],
        [8, 7, 0]
        
    ]

    print("Initial State:")
    print_board(initial_board)

    solution = solve_puzzle(initial_board)

    if solution is None:
        print("No solution found!")
    else:
        print("Solution found in", len(solution) - 1, "moves.")
        for i in range(len(solution)):
            print("Step", i)
            print_board(solution[i])

# Run the code
main()
