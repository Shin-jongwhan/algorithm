import random
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class adjacency_list: 
	def generate_random_al(self, nVertices, nEdges):
		# 인접 리스트를 위한 기본 딕셔너리 (기본값은 빈 리스트)
		al = defaultdict(list)
		
		edges = set()  # 중복 간선을 피하기 위한 집합

		while len(edges) < nEdges:
			# 무작위로 두 정점을 선택 (0부터 nVertices-1 범위에서)
			v1 = random.randint(0, nVertices - 1)
			v2 = random.randint(0, nVertices - 1)
			
			# 자기 자신에게 가는 간선은 허용하지 않음, 그리고 중복 간선을 피함
			if v1 != v2 and (v1, v2) not in edges and (v2, v1) not in edges:
				edges.add((v1, v2))
				al[v1].append(v2)
				al[v2].append(v1)  # 무방향 그래프일 경우

		# 키와 값 모두 오름차순으로 정렬
		sorted_al = {k: sorted(v) for k, v in sorted(al.items())}

		return sorted_al


	# 그래프를 그려주는 함수
	def draw_al_graph(self, al):
		G = nx.Graph()

		# 인접 리스트를 그래프에 추가
		for node, neighbors in al.items():
			for neighbor in neighbors:
				G.add_edge(node, neighbor)

		# 그래프 레이아웃 설정
		pos = nx.spring_layout(G)  # 노드 위치를 자동으로 결정 (spring layout)
		
		# 그래프 그리기
		plt.figure(figsize=(8, 6))
		nx.draw(G, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700, font_size=12)
		plt.title("Randomly Generated Graph")
		plt.show()


	def print_al(self, al) : 
		# 결과 출력
		for vertex, neighbors in al.items():
			print(f"{vertex}: {neighbors}")


	