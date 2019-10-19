import math
import numpy as np


def schedule(t):
    return 1.0 / math.log(t)


# this version works if you are minimizing an objective function, like what we do here for n-queen total conflicts
def simulated_annealing(problem):
    current = problem
    t = 2
    while True:
        temperature = schedule(t)
        # print('iteration:{}, temperature:{}'.format(t, temperature))
        if temperature == 0:
            # note that for the schedule used here, temperature will never reach zero
            return current, t

        if current.find_total_conflicts() == 0:
            return current, t

        random_successor = current.get_random_successor()
        if random_successor.find_total_conflicts == 0:
            return random_successor, t

        energy_difference = random_successor.find_total_conflicts() - current.find_total_conflicts()
        # print('energy_difference:{}'.format(energy_difference))

        # consider moving to the successor if it is better than the current status
        if energy_difference < 0:
            current = random_successor
        else:
            prob_of_accepting_bad_move = math.exp(-energy_difference/temperature)
            current = np.random.choice(a=[random_successor, current], p=[prob_of_accepting_bad_move,
                                                                         1-prob_of_accepting_bad_move])
        t += 1
