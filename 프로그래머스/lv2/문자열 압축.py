def solution(s):
    answer = len(s)
    
    for i in range(1, len(s) + 1):
        splitted = [s[j:j+i] for j in range(0, len(s), i)]
        
        temp = ''
        stack = [splitted[0]]
        for j in range(1, len(splitted)):
            curr = splitted[j]
            if curr != stack[-1]:
                if len(stack) > 1:                
                    temp += str(len(stack))
                temp += stack[-1]
                stack.clear()
            stack.append(curr)
        
        # 스택 비우기
        if len(stack) > 1:
            temp += str(len(stack))
        temp += stack[-1]
        
        answer = min(answer, len(temp))
                
    return answer