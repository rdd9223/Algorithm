import sys

input = sys.stdin.readline
blue = 0
white = 0


def divideAndConquer(paper, x, y, n):
    global blue, white
    isCut = 0

    for i in range(y, y + n):
        isCut += sum(paper[i][x : x + n])

    if isCut == n ** 2:
        blue += 1
    elif isCut == 0:
        white += 1
    else:
        divideAndConquer(paper, x, y, n // 2)
        divideAndConquer(paper, x + n // 2, y, n // 2)
        divideAndConquer(paper, x, y + n // 2, n // 2)
        divideAndConquer(paper, x + n // 2, y + n // 2, n // 2)
    return


if __name__ == "__main__":
    N = int(input())
    paper = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        paper.append(tmp)

    divideAndConquer(paper, 0, 0, N)

    print(white)
    print(blue)
