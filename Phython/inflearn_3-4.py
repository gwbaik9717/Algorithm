sample="""3
1 3 5
5
2 3 6 7 9"""

arr1 = list(map(int, sample.split("\n")[1].split(" ")))
arr2 = list(map(int, sample.split("\n")[3].split(" ")))

# 투포인터
i = 0
j = 0

answer = []

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        answer.append(arr1[i])
        i+=1
    elif arr1[i] > arr2[j]:
        answer.append(arr2[j])
        j+=1
    else:
        answer += [arr1[i]] * 2
        i+=1
        j+=1

if i != len(arr1):
    answer += arr1[i:]
elif j != len(arr2):
    answer += arr2[j:]

print(answer)