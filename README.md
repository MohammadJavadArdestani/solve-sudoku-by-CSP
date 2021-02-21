# solve sudoku by CSP
 here we have two kinds of sudoku puzzle first one is just a numeric n*n table and the other one contains colored cell <br>
 we slove tables as a CSP problem using Backtrack algorithm with forward Checking and MRV and Degree heuristics.<br>


## normal sudoku
there is just one rule here: Each number should be unique in its row and column.

### input:
in the first-line enter n(dimension of table) </br>
in the next n line put each num value in a row(you can put * for free cell)

#### example: 
7 </br>
7 2 6 \* \* \* 1</br>
\* \* \* \* 4 \* \*</br>
\* 3 \* \* 1 \* \*</br>
\* \* 2 \* \* \* 7</br>
1 \* 7 \* 2 \* \*</br>
\* 6 \* \* \* \* 2</br>
\* \* \* 3 \* \* \*</br>

#### output:
[7, 2, 6, 4, 5, 3, 1]</br>
[3, 7, 5, 2, 4, 1, 6]</br>
[6, 3, 4, 7, 1, 2, 5]</br>
[4, 1, 2, 6, 3, 5, 7]</br>
[1, 4, 7, 5, 2, 6, 3]</br>
[5, 6, 3, 1, 7, 4, 2]</br>
[2, 5, 1, 3, 6, 7, 4]</br>

## colored sudoku
1- Each number should be unique in its row and column.<br>
2- each cell must contain a color s.t for every two adjacent cells if a cell has a greater number, then its color should have more priority over that adjacent

### input:
in the first-line enter m, n(number of colors and dimension of table)</br>
the second line contains m colors from high priority to low </br>
in the next n line put each cell num and color in a row(you can put * for free cell, and # for colorless cell).</br>

#### example: </br>
6 5</br>
r g b y p o</br>
4# 2b 3r 1# 5#</br>
2# 5# 1# 3# 4#</br>
5r 1# 4# 2# 3p</br>
3# 4# 2# 5# 1#</br>
1# 3# 5# 4# 2#</br>

#### output:</br>
color priority: o <  p <  y <  b <  g <  r</br>
result :</br>
[4g, 2b, 3r, 1o, 5b]</br>
[2o, 5g, 1o, 3p, 4y]</br>
[5r, 1o, 4p, 2o, 3p]</br>
[3p, 4y, 2o, 5b, 1o]</br>
[1o, 3p, 5b, 4y, 2p]</br>
