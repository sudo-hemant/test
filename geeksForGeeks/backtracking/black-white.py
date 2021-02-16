import atexit
import io
import sys


#  trying every position for the first knight and the position which 
# it cannot attack will be the position for the second kinght 


def solve(rows, columns):
    
    # to help in finding attackbale position by kinght to not write if conditions for 8 attackable positions
    # this can be made easy by using 2 arrays of size 8 each and the elements simultaneously 
    # representing x & y of attackable positions 
    positions1 = [-2, 2]
    positions2 = [-1, 1]

    total_pos = rows * columns
    result = 0
    mod = 1000000007
    
    for row in range(rows):
        for column in range(columns):
            attackable_pos = 1
            
            # to find attackable positions by kinght
            for i in positions1:
                for j in positions2:
                    if is_safe(row + i, column + j, rows, columns):
                        attackable_pos += 1
                    if is_safe(row + j, column + i, rows, columns):
                        attackable_pos += 1

            result += (total_pos - attackable_pos) % mod 

    return result % mod
            
# to check if the attackable position by knight is inside the board or not
def is_safe(x, y, r, c):
    if x >= 0 and y >= 0 and x < r and y < c:
        return True
    return False



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m,n = map(int,input().strip().split())
        print(solve(m,n))
