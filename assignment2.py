'''
크기가 N(> 0)인 정수들의 배열이 있다. 
이 배열내의 중복된 번호들을 제거하고 남은 번호들만을 저장하는 배열을 만드는 알고리즘을 구체적이고 명확하게 기술하라.
작성한 알고리즘의 시간복잡도를 θ(Theta)-표기로 나타내라.
'''


def deleteDuplicateElement(A):
    R = []

    for i in A:
        isDuplicated = 0

        for j in R:
            if i == j:
                isDuplicated = 1
                break

        if isDuplicated == 0:
            R.append(i)

    return R


if __name__ == '__main__':
    A = [1, 2, 6, 2, 3, 6, 8, 2, 2, 4, 5]

    R = deleteDuplicateElement(A)
    print(R)
