import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    parent_dict = [i for i in range(n + 1)]  # Initialize the parent dictionary

    for _ in range(n - 1):
        parent, child = map(int, sys.stdin.readline().strip().split())
        parent_dict[child] = parent

    target1, target2 = map(int, sys.stdin.readline().strip().split())

    def find_path_to_root(start):
        path = []
        while True:
            path.append(start)
            if parent_dict[start] == start:  # Reached the root
                break
            start = parent_dict[start]
        return path

    path1 = find_path_to_root(target1)
    path2 = find_path_to_root(target2)

    # Find the Lowest Common Ancestor
    for node in path1:
        if node in path2:
            print(node)
            break
