T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    def dfs(l, start, sum):
        global ans

        if sum == k:
            ans += 1
        elif l == n or sum > k:
            return
        else:
            for i in range(start, n):
                dfs(l+1, i+1, sum + nums[i])

    dfs(0, 0,  0)
    print(f'#{test_case} {ans}')