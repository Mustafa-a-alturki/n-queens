# N-QUEEN

N-Queen is approached as a Constraint Satisfaction Problem, where there are N queens placed on an NxN board, each queen
is attacked from any queen placed on the same row, column or diagonal. The solution to the problem is a placement of all
the N queens such that no attack is possible.

In this implementation, each queen is placed in a different column, thus eliminating attacks coming from the same column. 

## Definitions:
- queen i is the queen placed on the ith column.
- Xi refers to the row in which queen i is placed.
- an assignment to the problem is an of assignment to a subset of the variables.
- A solution to the problem is a compatible and complete assignment, i.e. an assignment to all variables where no attack is possible.

The problem can be solved using Local Search Algorithms, where the search is done in a search space of complete 
assignments, where each assignment is evaluated by an objective function indicating the total number of possible attacks.
 
A solution is a complete assignment with objective function value of zero.
 
Simulated Annealing and Min-Conflicts algorithms are used here to find such an assignment.  
   