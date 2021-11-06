def greedy(array, n):
    result = 0
    usedWork = [0, 0, 0, 0]

    for i in range(n):
        minValue = 0

        for k in range(n):
            if (usedWork[k] != 1):
                minValue = array[i][k]

        for j in range(n):
            if (array[i][j] < minValue and usedWork[j] != 1):
                minValue = array[i][j]

        for l in range(n):
            if minValue == array[i][l]:
                usedWork[l] = 1

        result += minValue

    return result
    

arr = [
    [5, 3, 6, 7],
    [4, 6, 2, 5],
    [6, 3, 5, 4],
    [9, 6, 8, 5]
]

print(greedy(arr, 4))