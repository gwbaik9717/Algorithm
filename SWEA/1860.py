T = int(input())

for test_case in range(1, T + 1):
    n, m, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    for i in range(n):
        total = (nums[i] // m) * k
        if total < i + 1:
            print(f'#{test_case} Impossible')
            break
    else:
        print(f'#{test_case} Possible')

