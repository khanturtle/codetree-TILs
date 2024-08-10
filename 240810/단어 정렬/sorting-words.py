n=int(input())
n_str=[]
for i in range(n):
    n_str.append(input())

n_str.sort()
for s in n_str:
    print(s)