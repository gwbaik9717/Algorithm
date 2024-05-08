def solution(k, ranges):
    answer = []
    ycoords = [k]
    
    while k != 1:
        if k % 2 == 0:
            k = k / 2
        else:
            k = (k * 3) + 1
        ycoords.append(k)
    
    for start, end in ranges:
        end = len(ycoords) - 1 + end
        area = 0
        
        if start > end:
            area = -1
        
        for i in range(start + 1, end + 1):
            area += (ycoords[i] + ycoords[i-1]) / 2
        
        answer.append(area)
    
    
    return answer