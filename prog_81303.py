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
            for _ in range(int(cmd[-1])):
                currentRow = currentRow.prev
        elif cmd[0] == 'D':
            for _ in range(int(cmd[-1])):
                currentRow = currentRow.next
        elif cmd[0] == 'C':
            currentRow.isDeleted = True
            deletedHistory.append(currentRow)

            if currentRow.prev:
                currentRow.prev.next = currentRow.next
            if currentRow.next:
                currentRow.next.prev = currentRow.prev

            if currentRow.next == None:
                currentRow = currentRow.prev
            else:
                currentRow = currentRow.next

        elif cmd[0] == 'Z':
            recoverRow = deletedHistory.pop()
            recoverRow.isDeleted = False

            if recoverRow.prev:
                recoverRow.prev.next = recoverRow
            if recoverRow.next:
                recoverRow.next.prev = recoverRow

    for row in rows:
        if row.isDeleted == False:
            answer += 'O'
        else:
            answer += 'X'

    return answer
