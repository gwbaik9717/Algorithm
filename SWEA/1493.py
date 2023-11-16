T = int(input())

for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    def getCoord(n):
        sum = 0
        i = 0

        while sum < n:
            i += 1
            sum += i

        d = n - (sum - i) - 1
        start = (1 + d, i - d)

        return start

    def getSum(p, q):
        return (p[0] + q[0], p[1] + q[1])

    def convert(coord):
        (x, y) = coord
        n = x + y - 1

        return int(n * (n - 1) / 2) + x

    addrP = getCoord(p)
    addrQ = getCoord(q)

    ans = convert(getSum(addrP, addrQ))
    print(f'#{test_case} {ans}')