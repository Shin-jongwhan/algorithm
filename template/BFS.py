from collections import deque
from general import adjacency_list

al_m = adjacency_list()

# BFS 함수 정의
def bfs(graph, start):
	visited = set()  # 방문한 노드를 추적하기 위한 집합
	queue = deque([start])  # 탐색할 노드를 위한 큐
	
	while queue:
		node = queue.popleft()  # 큐에서 첫 번째 노드를 추출
		if node not in visited:
			print(node, end=" ")  # 방문한 노드를 출력
			visited.add(node)  # 노드를 방문 처리
			queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)


def bfs_test(nStart = 1, nVertices = 5, nEdges = 6) : 
	start = 1
	print("시작 지점 :", start)
	# 그래프를 인접 리스트로 표현
	al = al_m.generate_random_al(nVertices, nEdges)
	#draw_al_graph(al)
	al_m.print_al(al)

	print("방문 순서")
	bfs(al, start)


bfs_test()