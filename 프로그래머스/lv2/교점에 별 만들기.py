from itertools import combinations

def get_intersection(line1, line2):
    a, b, e = line1
    c, d, f = line2
    
    if a*d - b*c == 0:
        return
    
    x = (b*f - e*d) / (a*d - b*c)
    y = (e*c - a*f) / (a*d - b*c)
    
    if int(x) == x and int(y) == y:
        return int(x), int(y)

def solution(line):
    answer = []
    intersections = set()
    combis = combinations(line, 2)
    
    for combi in combis:
        intersection = get_intersection(combi[0], combi[1])
        
        if intersection:
            intersections.add(intersection)
    
    w1, w2 = min(intersections, key = lambda x : x[0])[0], max(intersections, key = lambda x : x[0])[0]
    h1, h2 = min(intersections, key = lambda x : x[1])[1], max(intersections, key = lambda x : x[1])[1]
    
    # 별을 포함하는 최소한의 크기 배열 생성
    answer = [['.'] * (w2 - w1 + 1) for _ in range((h2 - h1 + 1))]

    # 그림의 시작점을 기준으로 교점 위치 "*" 변환
    for x, y in intersections:
        print(x, y, y-h1, x-w1)
        answer[y-h1][x-w1] = '*'
    
    answer.reverse()
    
    return [''.join(a) for a in answer]