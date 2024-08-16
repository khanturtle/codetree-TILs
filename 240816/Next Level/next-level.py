class Lv:
    def __init__(self,id='codetree',level=10):
        self.id=id
        self.level=level

lv1=Lv()

print('user '+ lv1.id +' lv '+ str(lv1.level))

id,level = tuple(input().split())  
lv1 = Lv(id,level)

print('user '+ lv1.id +' lv '+ lv1.level)