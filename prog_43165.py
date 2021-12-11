# 타겟넘버
# BFS를 통한 풀이


def solution(numbers, target):
    answer = 0
    memoization = [0]

    # 모든 경우를 메모이제이션에 저장
    for number in numbers:
        tmp = []
        for value in memoization:
            tmp.append(value + number)
            tmp.append(value - number)
        memoization = tmp

    # 메모이제이션된 모든 결과중에서 target에 해당하는 값 카운트
    for value in memoization:
        if value == target:
            answer += 1

    return answer
