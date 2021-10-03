"""
크기가 n인 배열의 요소들 중 과반보다 더 많이 같은 요소가 있다면 과반수 요소를 가진다고 말한다. 
예를 들면, 한 배열 내에 54, 23, 97, 23, 23, 80, 23, 67, 23이 저장되어 있다면 이 배열은 크기가 9이고 배열 내에 23이 5개 있으므로 과반수 요소(23)를 가진다.

크기가 n 인 배열 내에 과반수 요소가 있으면 그 요소를 알려 주고 없으면 과반수 요소가 없다고 알려 주어야 한다. 
‘A[i] = A[j]’와 같이 두 개의 배열 요소들이 같은지를 상수(O(1)) 시간에 알 수 있다고 가정한다. 
이 문제를 O(n log n) 시간에 해결하는 분할정복 알고리즘을 작성하라. 
(힌트: 배열 A를 같은 크기의 두 개의 부분 배열(A_1과 A_2)로 분할하라. 
부분 배열 A_1의 과반수 요소와 부분 배열 A_2의 과반수 요소를 아는 것이 배열 A의 과반수 요소를 찾는 데 도움을 준다.)
"""


def countFrequency(arr, element):
    count = 0

    for i in range(len(arr)):
        if arr[i] == element:
            count += 1

    return count


def divideAndConquer(arr, low, high):
    if low == high:
        return arr[low]

    mid = (high + low) // 2

    lowElement = divideAndConquer(arr, low, mid)
    highElement = divideAndConquer(arr, mid + 1, high)

    lowElementCount = countFrequency(arr, lowElement)
    highElementCount = countFrequency(arr, highElement)

    if lowElementCount < highElementCount:
        return highElement

    return lowElement


def findMostElement(arr):
    result = divideAndConquer(arr, 0, len(a) - 1)

    if countFrequency(arr, result) == 1:
        return "과반수 요소가 없습니다."

    return result


a = [54, 23, 97, 23, 23, 80, 23, 67, 23]

print(findMostElement(a))
