def same_arr(n,a_arr,b_arr):
    for i in range (n):
        if(a_arr[i]!=b_arr[i]):
            return False
    return True

n=int(input())
a_arr=list(map(int,input().split()))
b_arr=list(map(int,input().split()))

a_arr.sort()
b_arr.sort()

if(same_arr(n,a_arr,b_arr)):
    print("Yes")
else:
    print("No")