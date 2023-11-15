from itertools import combinations

T = int(input())

def pow(a, n):
    if n == 1:
        return a

    if n % 2 == 0:
        return pow(a, n / 2) ** 2 % 1234567891
    else:
        return (pow(a, n // 2) ** 2) * a % 1234567891

for test_case in range(1, T + 1):
    n, r = map(int, input().split())

    factorial = [1] * 1000001

    for i in range(1, len(factorial)):
        factorial[i] = (i * factorial[i-1]) % 1234567891

    ans = pow(factorial[n-r] * factorial[r], 1234567891 - 2) * factorial[n] % 1234567891

    print(f'#{test_case} {ans}')
