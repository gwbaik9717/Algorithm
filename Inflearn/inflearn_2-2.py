sample = """2
6 2 5 3
5 2 7 3 8 9
15 3 10 3
4 15 8 16 6 6 17 3 10 11 18 7 14 7 15"""

inputs = sample.split('\n')
tcs = int(inputs[0])


for i in range(tcs):
    tc = list(map(lambda x: list(map(int, x.split(' '))), inputs[i*2+1:i*2+3]))
    n,s,e,k = tc[0]
    sliced = tc[1][s-1:e]
    sliced.sort()
    print(f'''#{i+1}''', sliced[k-1])