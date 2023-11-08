sample="""4 11
802
743
457
539"""

inputs = sample.split("\n")
[k, n] = map(int, inputs[0].split(" "))
nums = list(map(int, inputs[1:]))

left = 1
right = max(nums)
mid = (left + right) // 2

while left <= right:
    s = sum(list(map(lambda x: x // mid, nums)))
    
    if s < n:
        right = mid - 1
    else:
        left = mid + 1

    mid = (left + right) // 2

print(right)