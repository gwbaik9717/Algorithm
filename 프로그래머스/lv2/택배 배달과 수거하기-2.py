def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    have_to_deliver, have_to_pick = 0, 0
    
    for i in range(n):
        have_to_deliver += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deliver > 0 or have_to_pick > 0:
            answer += (n-i) * 2
            have_to_deliver -= cap
            have_to_pick -= cap

    return answer