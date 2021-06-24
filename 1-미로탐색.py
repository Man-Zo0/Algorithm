from collections import deque

mat = []

n,m = map(int,input().split())
visited = [[False for _ in range(m)]for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

for _ in range(n):
	mat.append([int(x) for x in list(input())])
	
def bfs():
	
	visited = [[False for _ in range(m)]for _ in range(n)]
	que = deque([[0,0,1]])
	
	while que:
		y,x,cnt = que.popleft()
		
		if y == n-1 and x == m-1:
			return cnt
		
		for i in range(4):
			nextx = x + dx[i]
			nexty = y + dy[i]
			
			if 0<=nexty<n and 0<=nextx<m and mat[nexty][nextx] and not visited[nexty][nextx]:
				que.append([nexty,nextx,cnt+1])
				visited[nexty][nextx] = True
	

print(bfs())
