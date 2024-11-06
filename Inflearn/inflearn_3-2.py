import re, math
sample="""g25ft"""

def dividers(num):
    st = set()
    for i in range(1, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            st.add(i)
            st.add(num/i)
    return len(st)     
        
num = int("".join(re.split("[a-zA-Z]", sample)))
print(num)
print(dividers(num))