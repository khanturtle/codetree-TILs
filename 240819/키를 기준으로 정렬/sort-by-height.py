n=int(input())
people = [
    tuple(input().split())
    for _ in range(n)
]
people.sort(key=lambda x: x[1])

for person in people:
    a,b,c=person
    print(a,b,c)