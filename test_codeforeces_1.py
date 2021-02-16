
def next_permuatition(permutation):
    
    inversion_point = len(permutation) - 2
    while inversion_point >= 0 and permutation[inversion_point] >= permutation[inversion_point + 1]:
        inversion_point -= 1
    
    for i in reversed(range(inversion_point + 1, len(permutation))):
        if permutation[i] > permutation[inversion_point]:
            permutation[i], permutation[inversion_point] = permutation[inversion_point], permutation[i]
            break

    permutation[inversion_point + 1 : ] = reversed(permutation[inversion_point + 1 : ])


if __name__ == '__main__':

    n, q = [int(x) for x in input().split()]

    permutation = [] * n
    for i in range(1, n + 1):
        permutation.append(i)

    for _ in range(q):
        curr = [int(x) for x in input().split()]

        if curr[0] == 1:
            summ = 0
            for i in range(curr[1] - 1, curr[2]):
                summ += permutation[i]
            print(summ)
        
        else:
            for i in range(curr[1]):
                next_permuatition(permutation)
            

























    # t = int(input())
    # for _ in range(t):
    #     size = int(input())
    #     arr = [int(x) for x in input().split()]
    #     flag = 0

    #     for i in range(1, size - 1):
    #         if arr[i] > arr[i - 1] + arr[i + 1]:
    #             flag = 1
    #             break
        
    #     if flag == 1:
    #         print('NO')
    #     else:
    #         print('YES')

        
    

















    # def delivery(i, max_a, sum_b, a, b, min_cost):
    #     if i == -1:
    #         min_cost[0] = min(min_cost[0], max(max_a, sum_b))
    #         return
        
    #     delivery(i - 1, max(max_a, a[i]), sum_b, a, b, min_cost)
    #     delivery(i - 1, max_a, sum_b + b[i], a, b, min_cost)


    # t = int(input())
    # # t = 1
    # for _ in range(t):
    #     size = int(input())
    #     # size = 2
    #     a = [int(x) for x in input().split()]
    #     # a = [10, 10]
    #     b = [int(x) for x in input().split()]
    #     # b = [1, 2]

    #     min_cost = [float('inf')]
    #     delivery(size - 1, float('-inf'), 0, a, b, min_cost)
    #     print(min_cost[0])