def solution(user_id, banned_id):
    answer = 0
    
    def get_candidates(bid):
        rv = dict()
        
        for uid in user_id:
            
            # compare by length
            if len(uid) != len(bid):
                continue
            
            for i, bchar in enumerate(bid):
                if bchar != '*':
                    if bchar != uid[i]:
                        break
            else:
                rv[uid] = True
        
        return rv
    
    candidates = [get_candidates(bid) for bid in banned_id]
    
    ans = 0
    keys_set = set()
    
    def dfs(lv, cur):
        nonlocal ans
        nonlocal keys_set
        
        if lv == len(candidates):
            ans += 1
            sorted_keys= sorted(list(cur.keys()))
            keys_set.add(",".join(sorted_keys))
            return
        
        for candidate in candidates[lv].keys():
            if candidate not in cur:
                cur[candidate] = True
                dfs(lv+1, cur)
                del cur[candidate]
    
    dfs(0, dict())
    
    answer = len(keys_set)
    
    return answer