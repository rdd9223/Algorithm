# 피보나치
import sys

input = sys.stdin.readline

memory = [0, 1] + [0] * 90


def fibo(n):
    if memory[n] == 0 and n != 0:
        memory[n] = fibo(n-1) + fibo(n-2)
    return memory[n]


num = int(input())
print(fibo(num))
