def yoon_year(y):
    if(y%4==0):
        if(y%100==0):
            if(y%400==0):
                return True
            return False
        return True

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

def is_exist_yoon(m,d):
    if(m<=12):
        if(m==2):
            if(d<=29):
                return True
        elif(m==4 or m==6 or m==9 or m==11):
            if(d<=30):
                return True
        else:
            if(d<=31):
                return True
    return False

def season(m):
    if(m>=3 and m<=5):
        return 'Spring'
    if(m>=6 and m<=8):
        return 'Summer'
    if(m>=9 and m<=11):
        return 'Fall'
    if(m==12 or m==1 or m==2):
        return 'Winter'

y,m,d = map(int,input().split())

if(yoon_year(y)):
    if(is_exist_yoon(m,d)):
        print(season(m))
    else:
        print(-1)
else:
    if(is_exist(m,d)):
        print(season(m))
    else:
        print(-1)