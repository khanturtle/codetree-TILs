n = int(input())
students=[]
for _ in range(n):
    data = input().split()
    name = data[0]
    kor = int(data[1])
    eng = int(data[2])
    math = int(data[3])
    students.append((name, kor, eng, math))

students.sort(key=lambda x: (-x[1], -x[2], -x[3], x[0]))

for student in students:
    name, kor, eng, math = student
    print(name, kor, eng, math)