def is_exist(m,d):
    if(m<=12):
        if(m==2):
            if(d<=28):
                return True
        elif(m==4 or m==6 or m==9 or m==11):
            if(d<=30):
                return True
        else:
            if(d<=31):
                return True
    return False

m,d = map(int,input().split())

if(is_exist(m,d)):
    print('Yes')
else:
    print("No")