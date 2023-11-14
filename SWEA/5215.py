T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, calories = map(int, input().split())
    options = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    def dfs(lv, start, score):
        global  ans

        if lv <= calories:
            ans = max(ans, score)
            for i in range(start, n):
                [cs, ck] = options[i]
                dfs(lv + ck, i+1, score + cs)

    dfs(0, 0, 0)

    print(f'#{test_case} {ans}')