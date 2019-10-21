import sys
import random


# Class for the Conway's game of Life
class Life:
    def __init__(self, no_of_row, no_of_column, current_generation):
        self.no_of_row = no_of_row
        self.no_of_column = no_of_column
        self.current_generation = current_generation

        # Variable to hold next generation
        self.next_generation = [[0 for j in range(self.no_of_column)] for i in range(self.no_of_row)]

    # Function to check if the input grid is correct
    def Check_Grid(self):
        if len(self.current_generation) != self.no_of_row:
            return False
        for i in range(self.no_of_row):
            if len(self.current_generation[i]) != self.no_of_column:
                return False
            for j in range(self.no_of_column):
                if self.current_generation[i][j] not in [1, 0]:
                    return False
        return True

    # Function to check if every cell in the grid became Stable
    def Check_Stable(self):
        for i in range(self.no_of_row):
            for j in range(self.no_of_column):
                if self.current_generation[i][j] != self.next_generation[i][j]:
                    return False
        return True

    # Function to compute next generation
    def Compute_Next_Generation(self):
        for i in range(self.no_of_row):
            for j in range(self.no_of_column):
                # Finding row boundaries of neighbouring cells
                if i-1 >= 0:
                    initial_row = i-1
                else:
                    initial_row = i
                if i+1 <= self.no_of_row-1:
                    final_row = i+1
                else:
                    final_row = i

                # Finding column boundaries of neighbouring cells
                if j-1 >= 0:
                    initial_column = j-1
                else:
                    initial_column = j
                if j+1 <= self.no_of_column-1:
                    final_column = j+1
                else:
                    final_column = j

                # Calculating number of live neighbours
                no_of_live_neighbours = 0
                for k in range(initial_row, final_row+1):
                    for l in range(initial_column, final_column+1):
                        if k == i and l == j:
                            continue
                        if self.current_generation[k][l] == 1:
                            no_of_live_neighbours += 1
                
                # Appling the given conditions
                if no_of_live_neighbours <= 1:
                    self.next_generation[i][j] = 0
                elif no_of_live_neighbours == 2:
                    self.next_generation[i][j] = self.current_generation[i][j]
                elif no_of_live_neighbours == 3:
                    self.next_generation[i][j] = 1
                else:
                    self.next_generation[i][j] = 0
        return self.next_generation

    # Function to find Final Stable Grid
    def Find_Stable_Grid(self):
        # Checking if every element of the grid became stable
        while self.Check_Stable() == False:
            # Continue to Compute next generation
            
            # Making Next generation Current generation
            self.current_generation, self.next_generation = self.next_generation, self.current_generation

            self.Compute_Next_Generation()
        
        return self.current_generation


def main():
    print("Enter number of rows and columns of the grid separated by a space : ")
    no_of_row, no_of_column = map(int, input().split())
    
    # Variable to hold first generation
    matrix1 = [[0 for j in range(no_of_column)] for i in range(no_of_row)]

    # Choice
    print("Do you want random initialization of grid?")
    print("1. YES")
    print("2. I want to initialize the grid myself")
    choice = int(input())

    if choice == 1:
        for i in range(no_of_row):
            for j in range(no_of_column):
                matrix1[i][j] = random.randint(0,1)
                print(matrix1[i][j], end=" ")
            print("")
    
    elif choice == 2:
        print("Input the grid denoting 1 for living cell and 0 for empty cell")
        print("NOTE - Enter the row elements separated by space and rows separated by new line")

        # Loop to input the initial grid
        for i in range(no_of_row):
            try:
                matrix1[i] = list(map(int, input().split()))
            except:
                print("Wrong Input")
                sys.exit(0)
    
    else:
        print("Wrong Choice")
        sys.exit(0)
    
    # Object of class Life
    obj = Life(no_of_row, no_of_column, matrix1)
    
    # Checking if the Input Grid is Valid
    if obj.Check_Grid() == False:
        print("Wrong Input Grid")
        sys.exit()

    # Coumputing Resultant Colony
    stable_grid = obj.Find_Stable_Grid()

    print("Final Colony:")
    for i in range(no_of_row):
        for j in range(no_of_column):
            print(stable_grid[i][j], end=' ')
        print("")

if __name__ == "__main__":
    main()