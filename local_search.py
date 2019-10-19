import numpy as np


def min_conflict(nqueen):
    steps = 0
    while True:
        if nqueen.find_total_conflicts() == 0:
            return nqueen, steps
        conflicting_variable = nqueen.select_conflicting_queen()
        conflicts = []
        for v in range(len(nqueen.positions)):
            conflicts.append(nqueen.conflicts(conflicting_variable, v))

        min_num_of_conflicts = np.min(conflicts)
        possible_val = []
        for idx, val in enumerate(conflicts):
            if conflicts[idx] == min_num_of_conflicts:
                possible_val.append(idx)
        value = np.random.choice(possible_val)

        nqueen.positions[conflicting_variable] = value
        steps += 1