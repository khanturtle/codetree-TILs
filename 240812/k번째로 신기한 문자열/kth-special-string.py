n,k,t = input().split()

arr=[]
ans_arr=[]

for i in range(int(n)):
    arr.append(input())

flag = 0

for s in arr:
    flag = 1

    if(len(t)>len(s)):
        flag = 0
    else:
        for i in range(len(t)):
            if(t[i]!=s[i]):
                flag = 0

    if(flag):
        ans_arr.append(s)

ans_arr.sort()
print(ans_arr[int(k)-1])