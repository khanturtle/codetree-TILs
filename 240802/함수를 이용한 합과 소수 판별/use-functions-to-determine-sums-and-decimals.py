def is_prime_and_num_even(a,b):
    ans = set()
    for i in range(a,b+1):
        flag = 1
        for j in range(2,i):
            if(i%j==0):
                flag = 0
        if(flag):
            ans.add(i)
    cnt = 0
    for i in ans:
        if((i%10 + (i//10)%10) %2==0):
            cnt+=1
    return cnt

a,b = map(int,input().split())
print(is_prime_and_num_even(a,b))