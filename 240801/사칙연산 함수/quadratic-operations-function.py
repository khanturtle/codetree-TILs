def operate(a,o,c):

    if(o=='+'):
        return int(a)+int(c)
    elif(o=='-'):
        return int(a)-int(c)
    elif(o=='*'):
        return int(a)*int(c)
    elif(o=='/'):
        return int(a)//int(c)
    else:
        return False

a,o,c = input().split()

if(operate(a,o,c)==False):
    print('False')
else:
    print(str(a) + ' ' + o + ' ' + str(c) + ' = ' + str(operate(a,o,c)))