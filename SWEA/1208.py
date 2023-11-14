from heapq import heappush, heappop

for test_case in range(1, 11):
    d = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    for _ in range(d):
        maximum = nums[-1]
        minimum = nums[0]

        if maximum != minimum:
            nums.pop()
            nums.pop(0)

            nums.append(maximum - 1)
            nums.append(minimum + 1)
            nums.sort()
        else:
            break

    print(f'#{test_case} {max(nums) - min(nums)}')