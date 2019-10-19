N-QUEEN

N-Queen is approached a Constraint Satisfaction Problem, where there are N queens placed on a NxN board, each queen
is attacked from any queen placed on the same row, column or diagonal. The solution to the problem is a placement of all
the N queens such that no attack is possible.

In this implementation, each queen is placed in a column. 
Let Xi be a variable indicating the row in which queen i is placed in column i, an
assignment to the problem is an of assignment to a subset of the variables.

The problem can be solved by Local Search Algorithms, where the search is done in a search space of complete 
assignments, i.e. assignments where all variables Xi are assigned, and each assignment is evaluated by an objective
function indicating the total number of possible attacks. 
A solution is a complete assignment with objective function value of zero. 
Simulated Annealing and Min-Conflicts algorithms are used here to find such an assignment.  
