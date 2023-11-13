
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split()))
    ans = 0

    for i in range(2, n-2):
        leftH = max(buildings[i-1], buildings[i-2])
        rightH = max(buildings[i+1], buildings[i+2])

        l = max(0, buildings[i]-leftH)
        r = max(0, buildings[i]-rightH)

        ans += min(l, r)

    print(f'#{test_case} {ans}')

