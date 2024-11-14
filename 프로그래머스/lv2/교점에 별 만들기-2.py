from itertools import combinations

def get_intersection(line_a, line_b):
    
    a, b, e = line_a
    c, d, f = line_b
    
    if (a*d - b*c) == 0:
        return None
    
    x, y = (b*f - e*d) / (a*d - b*c), (e*c - a*f) / (a*d - b*c)
    
    if is_int((x, y)):
       return (int(x), int(y))
    
    return None

def is_int(point):
    a, b = point
    if a == int(a) and b == int(b):
        return True
    
    return False

def render(points):
    sx, sy = min(map(lambda point: point[0], points)), min(map(lambda point: point[1], points))
    ex, ey = max(map(lambda point: point[0], points)), max(map(lambda point: point[1], points))
    
    result = [["." for _ in range(sx, ex+1)] for _ in range(sy, ey+1)]
    
    for px, py in points:
        result[py - sy][px - sx] = "*"
    
    return ["".join(row) for row in result][::-1]
    
    
def solution(lines):
    intersection_set = set()
    combis = combinations(lines, 2)
    
    for combi in combis:
        intersection = get_intersection(combi[0], combi[1])
        if intersection:
            intersection_set.add(intersection)
    
    return render(intersection_set)