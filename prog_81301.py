# 숫자 문자열과 영단어
# https://programmers.co.kr/learn/courses/30/lessons/81301

numDict = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


def solution(s):
    answer = s

    for key, value in numDict.items():
        answer = answer.replace(value, key)

    return int(answer)
