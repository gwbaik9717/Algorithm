import sys
input = sys.stdin.readline
answer = 0

n = int(input().strip())
car_in = dict()

for i in range(n):
    car_number = input().strip()
    car_in[car_number] = i

car_out = [input().strip() for _ in range(n)]

for i in range(n-1):
    car_number = car_out[i]
    past_ranking = car_in[car_number]
    
    for j in range(i+1, n):
        compare_car_number = car_out[j]
        past_compare_car_ranking = car_in[compare_car_number]

        if past_ranking > past_compare_car_ranking:
            answer += 1
            break

print(answer)