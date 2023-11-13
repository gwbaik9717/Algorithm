# 3
# 3
# 10 7 6
# 3
# 3 5 9
# 5
# 1 1 3 1 2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0

    stack = []

    while nums:
        maximum = max(nums)
        for i, num in enumerate(nums):
            if num < maximum:
                ans += abs(maximum - num)
            else:
                nums = nums[i+1:]
                break
    print(f'#{test_case} {ans}')