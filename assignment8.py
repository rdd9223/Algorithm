# 정해진 시간에 가장 많은 결혼식의 일정을 짜는 알고리즘
# 입력: times(첫번째 인덱스가 시작시간, 두번째 인덱스가 종료시간인 배열을 가지고있는 결혼식 이차원 배열), n(총 결혼식 수)
# 출력: result(최적의 결혼식 일정 배정을 기록한 이차원 배열)
def greedy(times, n):
    result = []

    # 끝나는 시간이 빠른대로 정렬, 끝나는 시간이 같은 경우, 시작하는 시간이 빠른대로 정렬
    times.sort(key=lambda x: (x[1], x[0]))

    # 정렬된 결혼식 리스트를 순회
    for i in range(n):
        # result배열의 현재 길이 저장
        resultLength = len(result)

        # 배정된 결혼식이 아무것도 없다면, 종료시간이 가장 빠른 결혼식을 집어넣는다.
        if resultLength == 0:
            result.append(times[i])
        # 배정된 결혼식 중 가장 늦은 종료시간이, 새로운 결혼식의 시작시간보다 작다면, 해당 결혼식을 다음 스케쥴로 배정함.
        elif result[resultLength - 1][1] < times[i][0]:
            result.append(times[i])

    # 최적의 결혼식 일정을 나열한 이차원 배열을 반환
    return result


times = [
    [1, 4],
    [3, 5],
    [0, 6],
    [5, 7],
    [3, 8],
    [5, 9],
    [6, 10],
    [8, 11],
    [8, 12],
    [2, 13],
    [12, 14],
]
n = 11

print("결혼식 일정 리스트: ", times)
result = greedy(times, n)
print("최적화된 결혼식 일정 리스트", result)
