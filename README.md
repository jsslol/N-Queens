# N-Queens
Genetic Algorithm Solution to the N-Queens problem. <br>
# Problem Description
In chess, at each turn a queen can move horizontally, vertically, or diagonally one or more spaces
until it reaches either the edge of the board (8x8 in regular chess) or another piece. When another
piece is encountered in any of the queen’s possible directions of travel, it is said to be threatened.
This program looks for solutions where queens are placed on the chess board such that no queen threatens any other queen. 
# Results 
Here are the average generations needed to find a solution, I used 1000 as the baseline because it
was the best fit in terms of time for higher numbers of queens to finish. The number of
generations needed was reduced drastically as the population increased but so did the amount of
time needed to finish. <br>
I also did testing on the mutation probability and was expecting a bit different of results but the
difference was relatively small until the probability was raised significantly. So it would seem it
has pretty minor effects on the overall outcome assuming small differences. <br>
I do not have much of a basis to judge how reasonable the data is but I do think the numbers
seem decent. If anything, they are on the low side of performance in terms of time to find
solution and number of generations. <br>
A screen shot of data collected will be included in the files as well. 
