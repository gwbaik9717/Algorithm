T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for t in range(1, T + 1):
    maximum = 0
    tn = int(input())
    nums = map(int, input().split())
    dic = dict()
    ans = 0

    for num in nums:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1

        maximum = max(maximum, dic[num])

    for key in dic:
        if dic[key] == maximum:
            ans = max(ans, key)
    print(f'#{t} {ans}')
