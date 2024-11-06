from collections import defaultdict
import copy 

def dfs(start, N, graph, breadcrumb):
    if len(breadcrumb) == N + 1:
        return breadcrumb
    else:
        for idx, nn in enumerate(graph[start]):
            graph[start].pop(idx)
            
            tmp = copy.deepcopy(breadcrumb)
            tmp.append(nn)
            
            result = dfs(nn, N, graph, tmp)
            
            if result:
                return result
            
            graph[start].insert(idx, nn)
    
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for [start, end] in tickets:
        graph[start].append(end)
    
    for key in graph:
        graph[key].sort()
    
    answer = dfs('ICN', len(tickets), graph, ['ICN'])
    
    
    return answer