sample = """8 99
23 87 65 12 57 32 99 81"""

inputs = sample.split("\n")
[n, m] = map(int, inputs[0].split(" "))
nums = list(map(int, inputs[1].split(" ")))

nums.sort()

left = 0
right = n-1
mid = (left + right) // 2

ans = 0

while left <= right:
    if m == nums[mid]:
        ans = mid
        break
    if m < nums[mid]:
        right = mid - 1
    else:
        left = mid + 1

    mid = (left + right) // 2

print(ans + 1)