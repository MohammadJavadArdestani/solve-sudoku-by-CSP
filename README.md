# Solve Sudoku as a Constraint Satisfaction Problem
 Here we have two kinds of sudoku puzzles first one is just a numeric n*n table, and the other one contains colored cells. <br>
 We solve tables as a CSP problem using the Backtrack algorithm with forward-checking and MRV and Degree heuristics. <br>


## Normal Sudoku
There is just one rule here: Each number should be unique in its row and column.

### Input:
In the first-line enter n(dimension of table) </br>
In the next n line put each num value in a row(you can put * for free cell)

#### Example: 
7 </br>
|   | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| A | 7 | 2 | 6 | * | * | * | 1 |
| B | * | * | * | * | 4 | * | * |
| C | * | 3 | * | * | 1 | * | * |
| D | * | * | 2 | * | * | * | 7 |
| E | 1 | * | 7 | * | 2 | * | * |
| F | * | 6 | * | * | * | * | 2 |
| G | * | * | * | 3 | * | * | * |

#### Output:
|   | A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|---|
| A | 7 | 2 | 6 | 4 | 5 | 3 | 1 |
| B | 3 | 7 | 5 | 2 | 4 | 1 | 6 |
| C | 6 | 3 | 4 | 7 | 1 | 2 | 5 |
| D | 4 | 1 | 2 | 6 | 3 | 5 | 7 |
| E | 1 | 4 | 7 | 5 | 2 | 6 | 3 |
| F | 5 | 6 | 3 | 1 | 7 | 4 | 2 |
| G | 2 | 5 | 1 | 3 | 6 | 7 | 4 |

## Colored Sudoku
1- Each number should be unique in its row and column.<br>
2- Each cell must contain a color s.t for every two adjacent cells. If a cell has a greater number, then its color should have more priority over that adjacent

### Input:
In the first line, enter m, n(number of colors and dimension of the table).<br>
The second line contains m colors from high priority to low.<br>
In the next n line put each cell num and color in a row (you can put * for free cell, and # for colorless cell).<br>

#### Example: </br>
6 5</br>
r g b y p o</br>
| 4# | 2b | 3r | 1# | 5# |
|----|----|----|----|----|
| 2# | 5# | 1# | 3# | 4# |
| 5r | 1# | 4# | 2# | 3p |
| 3# | 4# | 2# | 5# | 1# |
| 1# | 3# | 5# | 4# | 2# |

#### output:</br>
color priority: o <  p <  y <  b <  g <  r</br>
result :</br>
| 4g | 2b | 3r | 1o | 5b|
|--- |----|----|----|---|
| 2o | 5g | 1o | 3p | 4y|
| 5r | 1o | 4p | 2o | 3p|
| 3p | 4y | 2o | 5b | 1o|
| 1o | 3p | 5b | 4y | 2p|
