from general import adjacency_list

al_m = adjacency_list()

def dfs_stack(graph, start):
	visited = set()
	stack = [start]  # 시작 노드를 스택에 넣음

	while stack:
		node = stack.pop()  # 스택에서 노드를 꺼냄

		if node not in visited:
			visited.add(node)  # 방문 처리
			print(node, end=' ')  # 방문한 노드 출력

			# 인접한 노드를 스택에 추가 (역순으로 넣어서 스택에서 pop할 때 순서 맞추기)
			for neighbor in reversed(graph[node]):
				if neighbor not in visited:
					stack.append(neighbor)
	print("")


def bfs_test(nStart = 1, nVertices = 5, nEdges = 6) : 
	start = 1
	print("시작 지점 :", start)
	# 그래프를 인접 리스트로 표현
	al = al_m.generate_random_al(nVertices, nEdges)
	#draw_al_graph(al)
	al_m.print_al(al)

	print("방문 순서")
	dfs_stack(al, start)
	al_m.draw_al_graph(al)


bfs_test()