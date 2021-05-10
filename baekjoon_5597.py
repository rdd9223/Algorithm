import sys

# 빠른 입력을 위한 라이브러리 적용
input = sys.stdin.readline

# 낸 학생 리스트 선언
submittedStudents = []

# 28명 학생 입력
for i in range(28):
    studentNum = int(input())  # 정수형으로 입력받음
    submittedStudents.append(studentNum)  # 학생 리스트에 저장

# 전체 학생의 번호를 반복
for i in range(1, 31):
    if i not in submittedStudents:  # 번호가 만약 낸 학생에 포함되어있지 않다면
        print(i)  # 출력
