# 최소 스패닝 트리
import collections
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
edges = collections.defaultdict(list)
mst = []
result = 0

# 무향 그래프 생성
for _ in range(E):
    n1, n2, w = map(int, input().split())
    edges[n1].append([w, n1, n2])
    edges[n2].append([w, n2, n1])

# 초기 노드 설정
connectedEdges = [1]
# 그래프에서 초기 노드와 연결되는 간선 리스트
candidatedEdge = edges[1]
# 오름차순으로 정렬
heapq.heapify(candidatedEdge)

while candidatedEdge:
    # 가장 가중치가 적은 간선을 선택
    w, n1, n2 = heapq.heappop(candidatedEdge)
    # 이미 들르지 않은 곳이라면
    if n2 not in connectedEdges:
        connectedEdges.append(n2)  # 방문 기록
        mst.append([w, n1, n2])  # 최소신장트리에 삽입

        # node2에 해당하는 간선을 돌면서 다음 노드가 이미 연결되어 있지 않다면, 후보군 간선 리스트에 해당 간선을 추가
        for edge in edges[n2]:
            if edge[2] not in connectedEdges:
                heapq.heappush(candidatedEdge, edge)

for mstEdge in mst:
    result += mstEdge[0]

print(result)
