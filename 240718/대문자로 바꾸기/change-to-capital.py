b=[]
for _ in range(5):
    b.append(input().split())

for i in range(5):
    for j in range(3):
        print(b[i][j].upper(),end=" ")
    print()