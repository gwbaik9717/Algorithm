sample = """5
level
moon
abcba
soon
gooG"""

strs = map(lambda x: x.lower(), sample.split("\n")[1:])

for j, str in enumerate(strs):
    flag = True
    for i in range(len(str)//2):
        if(str[i] != str[-1 -i]):
            flag = False
            break
    if flag:
        print(f'''#{j+1}''', "YES")
    else:
        print(f'''#{j+1}''', "NO")