n=int(input())
arr=list(map(int,input().split()))

for i in range(n):
    if(i==0):
        print(arr[0],end=' ')
    elif(i%2==0):
        arr2=arr[0:i+1]
        arr2.sort()
        print(arr2[i//2],end=' ')