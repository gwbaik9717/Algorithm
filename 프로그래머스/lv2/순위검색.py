from bisect import bisect_left

class Node:
    def __init__(self, value=""):
        self.value = value
        self.children = dict()
        self.scores = []

class Trie:
    def __init__(self):
        self.head = Node()
        
    def add(self, info):
        cur = self.head
        for v in info[:-1]:  # traverse until the last part, excluding the score
            if v not in cur.children:
                cur.children[v] = Node(v)
            cur = cur.children[v]
        # Add score to the last node in the path
        score = int(info[-1])
        cur.scores.append(score)
        cur.scores.sort()  # keep scores sorted for binary search
        
    def find(self, query):
        total = 0
        query = query.split(" and ")
        popped = query.pop()
        query += popped.split()

        def dfs(lv, cur):
            nonlocal total 
            if lv == 4:  # Last level - score
                if query[lv] == '-':
                    total += len(cur.scores)
                else:
                    threshold = int(query[lv])
                    idx = bisect_left(cur.scores, threshold)
                    total += len(cur.scores) - idx
                return

            if query[lv] == '-':
                for child in cur.children.values():
                    dfs(lv + 1, child)
            elif query[lv] in cur.children:
                dfs(lv + 1, cur.children[query[lv]])

        dfs(0, self.head)
        return total

def solution(infos, queries):
    answer = []
    trie = Trie()
    
    # save in trie
    for info in infos:
        trie.add(info.split())
    
    # process queries
    for query in queries:
        answer.append(trie.find(query))
        
    return answer
