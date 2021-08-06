# 가운데를 말해요
import heapq
import sys

input = sys.stdin.readline

N = int(input())
maxHeap = []
minHeap = []
result = []

for _ in range(N):
    num = int(input())

    if len(minHeap) == len(maxHeap):
        heapq.heappush(maxHeap, (-num, num))
    else:
        heapq.heappush(minHeap, num)

    if len(minHeap) != 0 and maxHeap[0][1] > minHeap[0]:
        maxNum = heapq.heappop(maxHeap)[1]
        minNum = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, (-minNum, minNum))
        heapq.heappush(minHeap, maxNum)

    result.append(maxHeap[0][1])

for i in result:
    print(i)

# 참고
'''
파이썬 힙 기본: https://www.daleseo.com/python-heapq/
해설: https://regularmember.tistory.com/142
'''
