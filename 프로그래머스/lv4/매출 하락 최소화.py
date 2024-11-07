def solution(sales, links):
    n = len(sales)
    tree = [[] for _ in range(n + 1)]

    # Build the tree structure
    for parent, child in links:
        tree[parent].append(child)

    # Add a dummy root to cover the root node (1) in calculations
    tree[0].append(1)

    dp = [[0] * 2 for _ in range(n + 1)]

    def dfs(node):
        # If it's a leaf node, base cases for dp
        if not tree[node]:
            dp[node][1] = sales[node - 1]  # Cost if this node attends
            dp[node][0] = 0  # Cost if this node doesn't attend
            return

        attend_cost = sales[node - 1]
        dp[node][1] = attend_cost  # Initializing if this node attends

        extra_cost = float('inf')  # To ensure at least one child attends if the node doesn’t
        total_cost = 0

        # Traverse children
        for child in tree[node]:
            dfs(child)

            # Add the minimum cost of each child, whether they attend or not
            total_cost += min(dp[child][0], dp[child][1])

            # Track the minimum extra cost if no child attended
            extra_cost = min(extra_cost, dp[child][1] - min(dp[child][0], dp[child][1]))

        dp[node][0] = total_cost + (0 if extra_cost == float('inf') else extra_cost)
        dp[node][1] += total_cost  # Add the cost if the node itself attends

    # Run DFS from the dummy root
    dfs(0)

    # Return the minimum cost for the actual root node (1)
    return min(dp[1])

