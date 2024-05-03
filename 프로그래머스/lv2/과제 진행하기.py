def convert_to_timestamp(string):
    hh, mm = map(int, string.split(":"))
    return hh * 60 + mm
def solution(plans):
    answer = []
    
    plans = list(map(lambda x: [x[0], convert_to_timestamp(x[1]), int(x[2])], plans))
    sortedPlans = sorted(plans, key = lambda x : x[1])
    
    wait_list = []
    current_plan = sortedPlans[0]
    
    for new_plan in sortedPlans[1:]:
        nn, ns, nd = new_plan    
        cn, cs, cd = current_plan
        
        if cs + cd > ns:
            current_plan[2] = cs + cd - ns
            wait_list.append(current_plan)
        
        # 남은 시간이 있으면
        else:
            answer.append(current_plan[0])
            
            ct = cs + cd
            while wait_list:
                wn, ws, wd = wait_list.pop()
                
                if ct + wd <= ns and ct < ns:
                    answer.append(wn)
                    ct += wd
                else:
                    wait_list.append([wn, ws, cs + cd + wd - ns])
                    break
        
        current_plan = new_plan
    
    answer.append(current_plan[0])
    
    while wait_list:
        answer.append(wait_list.pop()[0])
    
    
    return answer