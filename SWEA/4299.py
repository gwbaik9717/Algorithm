from datetime import datetime
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    d, h, m = map(int, input().split())
    date1 = datetime.strptime('2011.11.11 11:11', '%Y.%m.%d %H:%M')
    date2 = datetime.strptime(f'2011.11.{d} {h}:{m}', '%Y.%m.%d %H:%M')
    dur = (date2 - date1).total_seconds()/60

    if dur < 0:
        print(f'#{test_case} -1')
    else:
        print(f'#{test_case} {round(dur)}')