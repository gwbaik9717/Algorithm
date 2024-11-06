import math
sample = """5
32 55 62 3700 250"""

nums = sample.split("\n")[1].split(" ")


def reverse(x):
    return int(x[::-1])

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(x + 1))):
        if(x % i == 0):
            return False
    else:
        return True

for num in nums:
    reversed = reverse(num)
    if(isPrime(reversed)):
        print(reversed, end=' ')