n= int(input())
days=[
    tuple(input().split())
    for _ in range(n)
]

rainy_days=[]
for d in days:
    if(d[2]=='Rain'):
        rainy_days.append(d)

rainy_days = sorted(rainy_days, key=lambda rainy_day: rainy_day[0])

print(rainy_days[0][0],end=' ')
print(rainy_days[0][1],end=' ')
print(rainy_days[0][2],end=' ')