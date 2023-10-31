sample="""10
1 0 1 1 1 0 0 1 1 0"""

nums = sample.split("\n")[1].split(" ")

answer = 0
cnt = 0

for num in nums:
    if num == "1":
        cnt += 1
    else:
        cnt = 0
    answer += cnt

print(answer)