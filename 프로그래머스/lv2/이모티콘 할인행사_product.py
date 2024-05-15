from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    discount_options = [10, 20, 30, 40]
    pds = product(discount_options, repeat = len(emoticons))
    
    for pd in pds:
        num_plus, sum_price = 0, 0
        
        for user_rate, user_price in users:
            temp = 0
            
            for i, discount in enumerate(pd):
                if discount >= user_rate:
                    temp += emoticons[i] * (100 - discount) / 100
                
            if temp >= user_price:
                num_plus += 1
            else:
                sum_price += temp
                    
        answer = max(answer, [num_plus, sum_price])  

    return answer