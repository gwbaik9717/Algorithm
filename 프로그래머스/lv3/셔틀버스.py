from collections import deque

def get_last_car(t, n):
    # 09:00
    start = 540
    last = start + (n-1) * t
    
    return last

def get_timestamp(t):
    hh, mm = map(int, t.split(":"))
    
    return hh * 60 + mm

def convert_timestamp(t):
    h = str(t // 60)
    m = str(t % 60)
    
    return f'{h.zfill(2)}:{m.zfill(2)}'

def get_last_group(n, t, m, sorted_q):
    last_group = []
    
    for i in range(n):
        time = t * i + 540
        
        for _ in range(m):
            
            if sorted_q and sorted_q[0] <= time:
                popped = sorted_q.popleft()
                
                if i == n-1:
                    last_group.append(popped)
            else:
                break
                
    return last_group

def solution(n, t, m, timetable):

    timestamps = list(map(get_timestamp, timetable))
    sorted_timestamps = deque(sorted(timestamps))

    last_group = get_last_group(n, t, m, sorted_timestamps)
    
    if len(last_group) < m:
        last_car = get_last_car(t, n)
        return convert_timestamp(last_car)
    
    
    max_time = last_group[-1] 
    return convert_timestamp(max_time - 1)
    