import sys

n, m = map(int, sys.stdin.readline().strip().split())

class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False  # This flag marks the end of a string

class Trie:
    def __init__(self):
        self.head = Node()
    
    def add(self, string):
        current = self.head
        for char in string:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_end = True  # Mark the end of the string
    
    def is_same(self, string):
        current = self.head
        for char in string:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end  # Return True only if it's the end of a valid string

trie = Trie()

# Adding strings to the trie
for _ in range(n):
    string = sys.stdin.readline().strip()
    trie.add(string)

ans = 0

# Checking for matches
for _ in range(m):
    string = sys.stdin.readline().strip()
    if trie.is_same(string):
        ans += 1

print(ans)
