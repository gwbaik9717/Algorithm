from datetime import datetime, time
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    m1, d1, m2, d2 = map(int, input().split())
    date1 = datetime.strptime(f'2015-{m1}-{d1}', '%Y-%m-%d')
    date2 = datetime.strptime(f'2015-{m2}-{d2}', '%Y-%m-%d')

    timedelta = date2 - date1
    print(f'#{i} {timedelta.days + 1}')

    # ///////////////////////////////////////////////////////////////////////////////////
