import sys

input = sys.stdin.readline

# submittedStudents = list(map(int, input().split('\n')))
submittedStudents = []

for i in range(28):
    studentNum = int(input())
    submittedStudents.append(studentNum)

for i in range(1, 31):
    if i not in submittedStudents:
        print(i)
