"""
N(≥ 3)개의 숫자들을 가진 정렬된 배열 A을 거의 N/3개의 숫자들을 가진 3 개의 부분배열로 분할하여 탐색하는 알고리즘을 작성하라. 
이 알고리즘은 찾는 숫자가 있을 가능성이 있는 부분배열에서 한 숫자를 탐색한다. 
이 부분배열을 필요하다면 다시 거의 같은 크기의 3개 부분배열로 분할한다.
주어진 숫자를 찾거나 주어진 숫자가 배열에 없다고 확인될 때까지 이 과정을 되풀이한다. 

n = 3^n
"""


def divideAndConquerAlgorithm(arr, start, end, key):
    lMid = start + ((end - start) // 3)
    rMid = end - ((end - start) // 3)

    if start >= end:
        print('찾는 숫자가 배열에 없습니다.')
    else:
        if key == arr[lMid]:
            print(f"찾는 숫자가 {lMid}인덱스에 있습니다")
        elif key == arr[rMid]:
            print(f"찾는 숫자가 {rMid}인덱스에 있습니다")
        elif key < arr[lMid]:
            divideAndConquerAlgorithm(arr, start, lMid, key)
        elif key < arr[rMid]:
            divideAndConquerAlgorithm(arr, lMid + 1, rMid, key)
        else:
            divideAndConquerAlgorithm(arr, rMid + 1, end, key)


S = [8, 13, 25, 28, 35, 41, 48, 53, 57, 60, 68, 72, 83, 85, 88, 92, 96, 99]
key = 99

divideAndConquerAlgorithm(S, 0, len(S), key)
