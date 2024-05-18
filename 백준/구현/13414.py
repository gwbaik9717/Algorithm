import sys
input = sys.stdin.readline

k, l = map(int, input().strip().split())
students = [input().strip() for _ in range(l)]

students_dic = dict()

for i, student in enumerate(students): 
    students_dic[student] = i

sorted_list = sorted(students_dic, key=lambda x: students_dic[x])

print("\n".join(sorted_list[:k]))