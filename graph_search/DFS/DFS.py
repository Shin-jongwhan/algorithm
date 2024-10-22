# 그래프를 인접 리스트로 표현
graph = {
	'A': ['B', 'C'],
	'B': ['A', 'D', 'E'],
	'C': ['A', 'F'],
	'D': ['B'],
	'E': ['B', 'F'],
	'F': ['C', 'E']
}


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


# DFS 실행
dfs_stack(graph, 'A')