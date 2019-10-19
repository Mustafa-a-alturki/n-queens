from n_queens import NQueen
from simulated_annealing import simulated_annealing
from local_search import min_conflict

if __name__ == '__main__':
    n = 8
    nqueen = NQueen(n)
    solution, steps = min_conflict(nqueen)
    print('Using Min-Conflict Algorithm')
    print('Number of Iterations:', steps)
    print(solution)

    nqueen = NQueen(n)
    solution, t = simulated_annealing(nqueen)
    print('Using Simulated Annealing Algorithm')
    print('Number of Iterations:', t)
    print(solution)