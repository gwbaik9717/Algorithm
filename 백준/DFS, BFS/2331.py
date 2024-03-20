import sys
from collections import deque

# 각 자리 수 합
def getSum(num, p):
    sum = 0
    for digit in str(num):
        sum += pow(int(digit), p)
    return sum


a, p = map(int, sys.stdin.readline().split())
arr = [a]

while True:
    newSum = getSum(arr[-1], p)
    
    if newSum in arr:
        while newSum in arr:
            arr.pop()
        break
    else:
        arr.append(newSum)

print(len(arr))