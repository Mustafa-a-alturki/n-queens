import numpy as np
import copy


class NQueen:
    def __init__(self, n, positions=None):
        if positions is not None:
            self.positions = np.int32(positions)
            n = len(self.positions)
        else:
            self.positions = []
            for i in range(n):
                self.positions.append(np.random.randint(0, n))

    def __str__(self):
        n = len(self.positions)
        board = np.zeros((n, n))
        for i, j in enumerate(self.positions):
            board[j][i] = 1
        return str(board) + '\n'

    def move(self, queen, new_position):
        if 0 <= new_position < len(self.positions):
            self.positions[queen] = new_position

    def get_random_successor(self):
        successor = copy.deepcopy(self)
        new_positions = []
        for _ in range(len(self.positions)):
            new_positions.append(np.random.randint(low=0, high=len(self.positions)))
        successor.positions = new_positions
        return successor

    def row_conflicts(self, queen):
        conflicts = 0
        for i, j in enumerate(self.positions):
            if i != queen:
                if j == self.positions[queen]:
                    conflicts += 1
        return conflicts

    def diagonal_conflicts(self, queen):
        conflicts = 0
        for i, j in enumerate(self.positions):
            if i != queen:
                # if the difference between x-coordinates and y-coordinates are the same
                if abs(i-queen) == abs(j - self.positions[queen]):
                    conflicts += 1
        return conflicts

    def find_conflicts(self, queen):
        conflict_count = 0
        conflict_count += self.row_conflicts(queen)
        conflict_count += self.diagonal_conflicts(queen)
        return conflict_count

    def find_total_conflicts(self):
        total_conflicts = 0
        for queen in range(len(self.positions)):
            total_conflicts += self.find_conflicts(queen)
        return total_conflicts

    def find_conflicts_in_candid_cell(self, queen, cell):
        old_position = self.positions[queen]
        self.move(cell)
        conflicts = self.find_conflicts(queen)
        self.move(old_position)
        return conflicts

    def find_conflicts_in_all_possible_cells(self, queen):
        conflicts_vec = np.zeros(len(self.positions))
        for cell in range(len(self.positions)):
            if cell != self.positions[queen]:
                conflicts_vec[cell] = self.find_conflicts_in_candid_cell(queen, cell)
            else:
                conflicts_vec[cell] = None

    def goal_test(self):
        for queen in len(self.positions):
            if self.find_conflicts(queen):
                return False
        return True

    def select_conflicting_queen(self):
        conflicting_queens = []
        for queen in range(len(self.positions)):
            if self.find_conflicts(queen) > 0:
                conflicting_queens.append(queen)
        return np.random.choice(conflicting_queens)

    def conflicts(self, queen, value):
        nqueen_copy = copy.deepcopy(self)
        nqueen_copy.positions[queen] = value
        return nqueen_copy.find_conflicts(queen)
