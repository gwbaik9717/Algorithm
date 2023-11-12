T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def calc():
    a, b, c = map(int, input().split())
    total = a * 35 + b * 45 + c * 20
    return total


for t in range(T):
    n, k = map(int, input().split())
    sums = [[calc(), j] for j in range(n)]
    sums.sort(key=lambda x: x[0], reverse=True)

    for i in range(10):
        for j in range(n // 10):
            sums[i * (n // 10) + j].append(grades[i])

    found = [x for x in sums if x[1] == k-1]
    print(f'#{t+1} {found[0][2]}')


