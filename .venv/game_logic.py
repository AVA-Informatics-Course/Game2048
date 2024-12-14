import random

class Game2048:
    """Represents the 2048 game with grid management, scoring, and moves."""

    def __init__(self, size=4):
        """Initializes the grid, score, and adds two starting tiles."""
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.score = 0
        self.generate_tile()
        self.generate_tile()

    def generate_tile(self):
        """Adds a new tile (2 or 4) to a random empty cell."""
        empty = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 2 if random.random() < 0.9 else 4

    def slide_and_merge(self, row):
        """Slides and merges"""
        non_zero = [num for num in row if num != 0]
        new_row, skip = [], False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                new_row.append(non_zero[i] * 2)
                self.score += non_zero[i] * 2
                skip = True
            else:
                new_row.append(non_zero[i])
        return new_row + [0] * (self.size - len(new_row))

    def get_max_tile(self):
        """Returns the maximum tile value in the grid."""
        return max(max(row) for row in self.grid)

    def move_left(self):
        """Performs a left move on the grid."""
        self.grid = [self.slide_and_merge(row) for row in self.grid]

    def move_right(self):
        """Performs a right move on the grid."""
        self.grid = [self.slide_and_merge(row[::-1])[::-1] for row in self.grid]

    def move_up(self):
        """Performs an upward move on the grid."""
        self.grid = list(map(list, zip(*self.grid)))
        self.move_left()
        self.grid = list(map(list, zip(*self.grid)))

    def move_down(self):
        """Performs a downward move on the grid."""
        self.grid = list(map(list, zip(*self.grid)))
        self.move_right()
        self.grid = list(map(list, zip(*self.grid)))

    def can_move(self):
        """Checks if any move is possible."""
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] == 0 or \
                   (r + 1 < self.size and self.grid[r][c] == self.grid[r + 1][c]) or \
                   (c + 1 < self.size and self.grid[r][c] == self.grid[r][c + 1]):
                    return True
        return False
