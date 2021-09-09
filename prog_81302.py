# 거리두기 확인하기
# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

# BFS를 이용한 풀이

import collections


def isKeptDistance(place):
    '''
    해당 면접장이 거리두기가 지켜지고 있는지 체크하는 함수
    '''
    pList = []  # 해당 테이블의 P위치를 저장하는 리스트
    q = collections.deque()

    # 모든 위치를 순회하며 P위치를 저장
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                pList.append([i, j])

    # P위치를 하나씩 순회하며 BFS
    for sx, sy in pList:
        q.append([sx, sy])  # 큐에 최초 P의 좌표 입력
        visited = []  # 방문 여부 확인 리스트
        distance = 0  # 최초 거리, 2이상 멀어지면 체크 안함

        while q:  # 큐가 빌때까지 순회
            nx, ny = q.popleft()  # 가까운 노드를 선택
            # 상하좌우 이동을 위한 리스트
            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]
            distance += 1  # 큐를 하나 비우며 이동할 때 마다 거리 증가

            if distance > 2:  # 거리가 2 이상(맨해튼 거리)이 된다면 순회 패스
                continue

            for i in range(4):  # 동서남북 들르기
                # 동서남북에 해당하는 새로운 좌표 값
                newX = nx + dx[i]
                newY = ny + dy[i]

                # 만약 검사할 좌표가 시험장을 벗어나거나, 이미 들렀거나, X(파티션)로 막혀있는 경우 패스
                if not (0 <= newX < 5
                        and 0 <= newY < 5
                        and [newX, newY] not in visited
                        and place[newX][newY] != 'X'):
                    continue

                # 만약 거리 내 다른 응시자가 있다면 종료
                if place[newX][newY] == 'P':
                    return False

                # 만약 이상이 없다면 방문기록을 남기고, 새로운 탐색 노드를 큐에 추가
                visited.append([nx, ny])
                q.append([newX, newY])

    # 모든 응시자가 거리두기를 잘 지켰다면 성공으로 리턴
    return True


def solution(places):
    answer = []

    # 모든 면접장을 순회
    for place in places:
        if isKeptDistance(place):
            answer.append(1)
        else:
            answer.append(0)

    return answer
