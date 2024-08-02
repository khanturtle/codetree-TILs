def rule(a,b):
    cnt = 0
    for i in range(a,b+1):
        if(i%2!=0 and i%10!=5):
            if(i%3==0 and i%9!=0):
                cnt = cnt
            else:
                cnt+=1
        
    return cnt

a,b=map(int,input().split())    
print(rule(a,b))