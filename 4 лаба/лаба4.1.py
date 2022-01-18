import random
G = []
v = []
v1 = []
N = 5
c = []
change = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

for i in range(N):
    G.append([])
    for j in range(N):
        G[i].append(random.choice(change))
        if(i == j):
            G[i][j] = 0
       
print('\n')

for i in range(N):
    for j in range(N):
        G[i][j] = G[j][i]
        print(G[i][j],end = '\t')
    print('\n')

def DFS(v):
    print(v + 1)
    vis[v] = 1
    for i in range(len(G)):
        if(G[v][i] == 1 and vis[i] == 0):
            DFS(i)

v = int(input("Введите вершину: ")) - 1
vis = []
for i in range(len(G)):
    vis.append(0)

DFS(v)
print('\n')
