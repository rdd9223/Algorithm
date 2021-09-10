'''
표 편집
https://programmers.co.kr/learn/courses/30/lessons/81303
LinkedList
'''


class Node:
    def __init__(self):
        self.isDeleted = False
        self.prev = None
        self.next = None


def solution(n, k, cmds):
    answer = ''
    rows = [Node() for _ in range(n)]
    deletedHistory = []

    for i in range(1, n):
        rows[i-1].next = rows[i]
        rows[i].prev = rows[i-1]

    currentRow = rows[k]

    for cmd in cmds:
        if cmd[0] == 'U':
            for _ in range(int(cmd[2:])):
                currentRow = currentRow.prev
        elif cmd[0] == 'D':
            for _ in range(int(cmd[2:])):
                currentRow = currentRow.next
        elif cmd[0] == 'C':
            deletedHistory.append(currentRow)
            currentRow.isDeleted = True

            up = currentRow.prev
            down = currentRow.next

            if up:
                up.next = down
            if down:
                down.prev = up
                currentRow = down
            else:
                currentRow = up

        else:
            recoveredRow = deletedHistory.pop()
            recoveredRow.isDeleted = False

            up = recoveredRow.prev
            down = recoveredRow.next

            if up:
                up.next = recoveredRow
            if down:
                down.prev = recoveredRow

    for row in rows:
        if row.isDeleted == False:
            answer += 'O'
        else:
            answer += 'X'

    return answer
