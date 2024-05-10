from itertools import combinations

def solution(relation):
    answer = 0
    h = len(relation)
    w = len(relation[0])
    col_indexes = [i for i in range(w)]
    candidates = []
    
    for i in range(1, w + 1):
        for combi in combinations(col_indexes, i):
            for candidate in candidates:
                if set(candidate).issubset(set(combi)):
                    break
            else:
                values_set = set()
                for row in relation:
                    values_set.add(''.join([row[i] for i in combi]))

                if len(values_set) == h:
                    candidates.append(combi)

    answer = len(candidates)
    return answer