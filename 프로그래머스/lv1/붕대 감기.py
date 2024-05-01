import math

def solution(bandage, health, attacks):
    current_time = 0
    current_health = health
    (bonus_dur, sec_hp, bonus_hp) = bandage
    
    for (attack_time, damage) in attacks:
        time_passed = attack_time - current_time - 1
        hp_gained = sec_hp * time_passed + math.floor(time_passed / bonus_dur) * bonus_hp
        
        
        # hp 충전
        current_health = min(health, current_health + hp_gained) - damage
        current_time = attack_time
        
        if current_health <= 0:
            return -1
    
    return current_health