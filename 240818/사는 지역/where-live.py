class person:
    def __init__(self,name,adnum,location):
        self.name=name
        self.adnum=adnum
        self.location=location

n=int(input())

people=[
    tuple(input().split())
    for _ in range(n)
]

names=[]
for p in people:
    names.append(p[0])
names.sort()    

for p in people:
    if(p[0]==names[-1]):
        print('name '+p[0])
        print('addr '+p[1])
        print('city '+p[2])