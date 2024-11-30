def solution(routes):
    answer = 1
    n = len(routes)
    sorted_routes = sorted(routes, key=lambda x: (x[0], x[1] - x[0]))
    
    intersection = sorted_routes[0]
    for i in range(1, n):
        left, right = sorted_routes[i]
        
        # 겹칠때
        if left <= intersection[1]:
            intersection = (left, min(right, intersection[1]))
        else:
            answer += 1
            intersection = (left, right)
    
    return answer