- a small python program using backtarcking to solve sudoku problems.
- the algorithm is essentially a depth-first search from left to right, top to bottom.
+ solve computes current puzzle shown on pygame gui.
+ reset changes everything back to original problem.
= clicking on numbers increments it, from 0-9. 0 being no number specified.
* classifies some solutions as valid even when they're not when assigning same numbers next to each other.
* happens to some not all numbers.
* however, works on all valid puzzle layouts