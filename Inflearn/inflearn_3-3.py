sample="""5 10
9 13
1 2
3 4
5 6
1 2
3 4
5 6
1 20
1 20"""

cards = [x for x in range(0, 21)]
inputs = map(lambda x: list(map(int, x.split(" "))), sample.split("\n"))


for a, b in inputs:
    reversed = cards[a:b+1]
    reversed.reverse()
    cards[a: b+1]=reversed


for card in cards[1:]:
    print(card, end=" ")