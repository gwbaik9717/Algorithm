def solution(data, col, row_begin, row_end):
    answer = -1
    
    # 정렬
    sorted_data = sorted(data, key=lambda x: (x[col - 1], -x[0]))
    
    for i in range(row_begin, row_end + 1):
        s_i = sum(map(lambda x: x % i, sorted_data[i - 1]))
        
        if answer == -1:
            answer = s_i
        else:
            answer = answer ^ s_i
        
    return answer