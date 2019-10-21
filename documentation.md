# Conway's Game of Life

**This is an implementation of a classic game "Conway's Game Of Life"**

## Rules

The simulation starts with an initial pattern of cells on the grid and computes successive
generations of cells according to the following rules:

1. A location that has zero or one neighbor will be empty in the next generation. If a cell was in
that location, it dies of loneliness.
2. A location with two neighbors is stable—that is, if it contained a cell, it still contains a cell. If
it was empty, it's still empty.
3. A location with three neighbors will contain a cell in the next generation. If it was unoccupied
before, a new cell is born. If it currently contains a cell, the cell remains. Good times.
4. A location with four or more neighbors will be empty in the next generation. If there was a
cell in that location, it dies of overcrowding.
5. The births and deaths that transform one generation to the next must all take effect
simultaneously. Thus, when computing a new generation, new births and deaths in that
generation don’t impact other births and deaths in that generation. To keep the two
generations separate, you will need to work on two versions of 3 the grid—one for the current 
generation, and a second that allows you to compute and store the next generation without
changing the current one.

## Running the program

1. Download the repository
2. To perform unit testing use - "python3 test_GameOfLife.py"
3. To Run the program use - "python3 GameOfLife.py"
    * Then follow the instructions on screen

## Sample 1

Enter number of rows and columns of the grid separated by a space : 
>3 3

Do you want random initialization of grid?
1. YES
2. I want to initialize the grid myself

>1
```
1 1 0
1 1 0 
0 0 0 

Final Colony:
0 0 0 
0 0 0 
0 0 0 
``` 

## Sample 2

Enter number of rows and columns of the grid separated by a space : 

>3 3

Do you want random initialization of grid?
1. YES
2. I want to initialize the grid myself

>2

Input the grid denoting 1 for living cell and 0 for empty cell
NOTE - Enter the row elements separated by space and rows separated by new line

>1 1 1

>1 1 1

>1 1 1

```
Final Colony:
0 0 0 
0 0 0 
0 0 0
```