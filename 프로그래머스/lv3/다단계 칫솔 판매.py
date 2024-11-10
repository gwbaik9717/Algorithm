import math

class Node:
    def __init__(self, parent):
        self.parent = parent
        self.count = 0

    def add_profit(self, tree, count):
        to_give = math.floor(count * 0.1)
        
        if to_give < 1:
            self.count += count
            return
        
        self.count += count - to_give
        
        if self.parent == '-':
            return
        
        parent_node = tree.get(self.parent)
        
        parent_node.add_profit(tree, to_give)

        
    
def solution(enroll, referral, seller, amount):
    answer = []
    
    tree = dict()
    
    for child, parent in zip(enroll[::-1], referral[::-1]):
                    
        tree[child] = Node(parent)
    
    for s, a in zip(seller, amount):
        current_node = tree.get(s)
        current_node.add_profit(tree, a * 100)
    
    answer = [tree[e].count for e in enroll]
    
    return answer