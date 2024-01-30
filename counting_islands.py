class IslandsCounter:
    def __init__(self, m, n, matrix):
        self.n_rows = m
        self.n_cols = n
        self.matrix = matrix
        self.island = 1
        self.ocean = 0

    def is_land(self, row: int, col: int) -> bool:
        # check is cell is land or ocean
        return self.matrix[row][col] == self.island

    def is_valid_row(self, row: int) -> bool:
        return 0 <= row < self.n_rows

    def is_valid_col(self, col: int) -> bool:
        return 0 <= col < self.n_cols

    def search_depth_first(self, row: int, col: int):
        if self.is_valid_row(row) and self.is_valid_col(col) and self.is_land(row, col):
            # not to revisit the same cell later
            self.matrix[row][col] = self.ocean
            for new_row, new_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                # run depth first search recursively
                self.search_depth_first(new_row, new_col)

    def get_n_islands(self):
        n_islands = 0
        for row in range(0, self.n_rows):
            for col in range(0, self.n_cols):
                if self.is_land(row, col):
                    n_islands += 1
                    self.search_depth_first(row, col)
        return n_islands


test_cases_inputs = [
    (3, 3, [[0, 1, 0], [0, 0, 0], [0, 1, 1]]),
    (3, 4, [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]]),
    (3, 4, [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1]])
]
test_cases_outputs = [2, 3, 2]

for test_input, test_output in zip(test_cases_inputs, test_cases_outputs):
    counter = IslandsCounter(*test_input)
    assert counter.get_n_islands() == test_output
