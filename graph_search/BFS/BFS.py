from collections import deque

# 그래프를 인접 리스트로 표현
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS 함수 정의
def bfs(graph, start):
    if graph == [] : 
        return None
    visited = set()  # 방문한 노드를 추적하기 위한 집합
    queue = deque([start])  # 탐색할 노드를 위한 큐
    
    while queue:
        node = queue.popleft()  # 큐에서 첫 번째 노드를 추출
        if node not in visited:
            print(node, end=" ")  # 방문한 노드를 출력
            visited.add(node)  # 노드를 방문 처리
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# 'A' 노드부터 BFS 탐색 시작
bfs(graph, 'A')
