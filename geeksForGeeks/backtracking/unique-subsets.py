

# didn't under the for loop properly

def AllSubsets(arr,n):
    
    def helper(i, temp, arr, n, result):
        if i >= n:
            result.append(temp[:])
            return
        
        advanced = i + 1
        
        while advanced < n and arr[advanced] == arr[i]:
            advanced += 1
        
        for j in range(advanced - i + 1):
            for k in range(j):
                temp.append(arr[i])
            
            helper(advanced, temp, arr, n, result)
            for k in range(j):
                temp.pop()
    
    
    arr.sort()
    result = []
    helper(0, [], arr, n, result)
    result.sort()
    return result


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int,input().strip().split()))
        result = AllSubsets(a,n)
        for i in range(len(result)):
            print("(",end="")
            size = len(result[i])
            for j in range(size-1):
                print(result[i][j],end=" ")
            if(size):
                print(result[i][size-1],end=")")
            else:
                print(")",end="")
        print()

