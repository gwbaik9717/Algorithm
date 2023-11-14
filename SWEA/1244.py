T = int(input())

checked = set()

for test_case in range(1, T + 1):
    num, limit = map(int, input().split())
    maximum = 0
    current = list(str(num))
    n = len(current)
    def dfs(lv):
        global  maximum

        if lv == limit:
            maximum = max(maximum, int(''.join(current)))
        else:
            for left in range(0, n-1):
                for right in range(left + 1, n):
                    current[left], current[right] = current[right], current[left]
                    next = int(''.join(current))

                    if (next, lv) not in checked:
                        checked.add((next, lv))
                        dfs(lv + 1)

                    current[left], current[right] = current[right], current[left]

    dfs(0)
    print(f'#{test_case} {maximum}')