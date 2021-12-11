def backtracking(N, arr):
    if len(arr) >= N:
        print(arr)
        return
    tmp0 = list(arr)
    tmp1 = list(arr)
    tmp0.append(0)
    tmp1.append(1)
    backtracking(N, tmp0)
    backtracking(N, tmp1)


backtracking(5, [])
