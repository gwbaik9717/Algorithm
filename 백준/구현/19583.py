import sys
input = sys.stdin.readline
answer = 0

def convert(time):
    hh, mm = map(int, time.split(":"))
    timestamp = hh * 60 + mm
    return timestamp

s, e, q = map(lambda x: convert(x), input().split())
participants = set()

while True:
    try:
        user_time, user_id = input().split()
        timestamp = convert(user_time)

        if timestamp <= s:
            # 참여자 담기
            participants.add(user_id)
        elif e <= timestamp <= q:
            if user_id in participants:
                answer += 1
                participants.remove(user_id)
    except:
        break

print(answer)