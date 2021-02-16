from collections import deque

def solve(n, maze):
    
    res = [ [0 for i in range(n)] for j in range(n)]
    
    if is_path(0, 0, res, n, maze):
        print_sol(n, res)
    else:
        print(-1)
    
    
def is_path(i, j, res, n, maze):
    # if we have reached the target
    if i == n - 1 and j == n - 1:
        res[i][j] = 1
        return True
    
    # if we are at safe position
    if is_safe(i, j, n, maze):
        # marking the correct pos as visited
        res[i][j] = 1
        # trying all possible jumps from current, 
        # in both horizontal or vertical
        for jump in range(1, maze[i][j] + 1):
            if jump >= n:
                break
            if is_path(i, j + jump, res, n, maze):
                return True
            if is_path(i + jump, j, res, n, maze):
                return True
        # if we haven't found our ans, we ll mark the curr as not viisted
        res[i][j] = 0
        return False
    return False
    
   
def is_safe(i, j, n, maze):
    if i >= 0 and j >= 0 and i < n and j < n and maze[i][j]:
        return True
    return False


def print_sol(n, sol):
    for i in range(n):
        for j in range(n):
            print(sol[i][j], end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        n = int(input())
        maze = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            maze[i] = [int(x) for x in input().strip().split()]
        solve(n, maze)
        t=t-1
