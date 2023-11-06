sample="""2 4 1 5 3 2 6
3 5 1 8 7 1 7
8 3 2 7 1 3 8
6 1 2 3 2 1 1
1 3 1 3 5 3 2
1 1 2 5 6 5 2
1 2 2 2 2 1 5"""

inputs = sample.split("\n")
graph = list(map(lambda x: x.split(" "), inputs))

def isPalindrome(str):
    return str == str[::-1]

ans = 0


for i in range(7):
    for j in range(3):
        str1 = "".join(graph[i][j:j+5])
        str2 = "".join(list(map(lambda row: row[i], graph))[j: j+5])

        if isPalindrome(str1):
            ans += 1
        if isPalindrome(str2):
            ans += 1


print(ans)