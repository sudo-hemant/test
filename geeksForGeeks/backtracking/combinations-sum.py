

def combinationalSum(arr, x):
    
    def find_sum(curr_pos, curr_arr, arr, length, find):
        # index out of range or greater than required value
        if curr_pos == length or find < 0:
            return
        # sum = required value
        if find == 0:
            result.append(curr_arr[:])
            return
        # appending the element to be included 
        curr_arr.append(arr[curr_pos])

        # including the curr element but not increasing the pos bcos we can include the same element multiple times
        find_sum(curr_pos, curr_arr, arr, length, find - curr_arr[-1])
        
        # removing the element added above to find a case when element 'll not be included
        curr_arr.pop()
        
        # not including the current element even once 
        find_sum(curr_pos + 1, curr_arr, arr, length, find)

    result = []
    arr = set(arr)
    arr = list(arr)
    arr.sort()     
    
    find_sum(0, [], arr, len(arr), x)
    
    return result



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        s = int(input())
        result = combinationalSum(a,s)
        if(not len(result)):
            print("Empty")
            continue
        for i in range(len(result)):
            print("(", end="")
            size = len(result[i])
            for j in range(size - 1):
                print(result[i][j], end=" ")
            if (size):
                print(result[i][size - 1], end=")")
            else:
                print(")", end="")
        print()

