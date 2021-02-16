

# 

from math import sqrt

def solve_sudoku(sudoku):
    
    def sudoku_helper(i, j, sudoku):
        if i == len(sudoku):
            return True
        
        # finds next position to be checked in sudoku
        ni, nj = i, j + 1
        if nj == len(sudoku):
            ni, nj = i + 1, 0
        
        # if the number is already there then check for the next position
        if sudoku[i][j]:
            if sudoku_helper(ni, nj, sudoku):
                return True
            else:
                return False
        # if the cell is empty
        else:
            for possible_no in range(1, 10):
                if is_safe(i, j, possible_no, sudoku):
                    sudoku[i][j] = possible_no    
                    if sudoku_helper(ni, nj, sudoku):
                        return True
                    sudoku[i][j] = 0
        return False
        
        
    if sudoku_helper(0, 0, sudoku):
        return True
    return False
    

def is_safe(x, y, possible_no, sudoku):
    
    for i in range(9):
        if sudoku[x][i] == possible_no:
            return False
        if sudoku[i][y] == possible_no:
            return False
    
    size = sqrt(len(sudoku))
    x = int(x // size * size)
    y = int(y // size * size)
    
    for i in range(3):
        for j in range(3):
            if sudoku[x + i][y + j] == possible_no:
                return False
    return True
    
    
def print_grid(arr):
    
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
    print()


if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        # row = [int(x) for x in input().strip().split()]
        # k = 0
        # for i in range(9):
        #     for j in range(9):
        #         grid[i][j] = row[k]
        #         k+=1
        
        grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]
            ]
        if(solve_sudoku(grid)==True):
            print_grid(grid)
        else:
            print("No solution exists")
        t = t-1
