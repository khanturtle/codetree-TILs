agents=[
    tuple(input().split())
    for _ in range(5)
]

score=[]
for agent in agents:
    score.append(int(agent[1]))
    
for agent in agents:
    if(int(agent[1])==min(score)):
        print(agent[0]+' '+ agent[1])