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
        print(G[i][j], end = '\t')
    print('\n')

def BFS(v):
	Vis[v] = 1
	queue.append(v)
	while(bool(queue)):
		s = queue[0]
		print(s+1)
		queue.pop(0)
		for i in range(len(G)):
			if(G[s][i] == 1 and Vis[i] == 0):
				queue.append(i)
				Vis[i] = 1

v = int(input('Введите вершину: ')) - 1

Vis = []
for i in range(len(G)):
	Vis.append(0)

queue = []

BFS(v)

print('\n')
