n=int(input())
n_list=list(map(int,input().split()))

n_list.sort()
for i in n_list:
    print(i,end=' ')
n_list=n_list[::-1]
print()
for i in n_list:
    print(i,end=' ')