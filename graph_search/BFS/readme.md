# BFS
### Breadth-First Search, 너비 우선 탐색
### <br/><br/>

## deque
#### 코드는 BFS.py 참고
### collection 모듈에 있는 기능 중 하나이다.
### double-ended queue, 양방향 큐라고 한다. 양쪽으로 값을 넣고 뺄 수 있어서 좋다.
### <br/>

### 값을 넣을 때는 오른쪽은 append(), 왼쪽은 appendleft()을 사용한다.
### 값을 뺄 때는 오른쪽은 pop(), 왼쪽은 popleft()를 사용한다.
### 뺀 값은 리턴을 받을 수 있다.
### <br/>

### 사실 deque는 기능상으로는 리스트와 같다고 보면 된다. 하지만 메모리적인 동작이 다르다.
### 예를 들면 이렇다.
```
# 리스트
ls = [1,2,3]    # dq = deque([1,2,3])
a = ls.pop()    # dq.pop()
b = ls.pop(0)    # dq.popleft()

```
### <br/>

### 아래 시간 복잡도 테이블을 참고하면 deque가 효율적이다.
#### https://wellsw.tistory.com/122
#### ![image](https://github.com/user-attachments/assets/b7630c52-46ab-4449-af25-01a911e5baef)
### <br/>

### 테스트(test.py)
### 실제로 테스트해보니 deque appendleft()는 시간이 O(1), 리스트는 O(n)인 것을 확인하였다.
### 리스트같은 경우 맨 앞에 추가하면, 메모리 주소를 한 칸씩 옮겨서 재할당이 필요하다(int가 기본적으로 32bit라서 32씩 이동함).
### deque는 연속된 메모리 주소로 이루어지지 않고 연속적이지 않은 블록으로 할당이 된다.
#### ![image](https://github.com/user-attachments/assets/7ba904b3-8049-4b3d-a83b-0525f7294098)
### <br/>

### 리스트와 비교했을 때 단점도 있다. deque는 왼쪽 끝에 값을 추가하거나 빼는 등의 이점은 있지만, 중간에 값을 인덱스로 조회하는 것은 느리다.
### 리스트는 인덱스 조회는 O(1)이다.
### <br/><br/><br/>

## BFS 구현 방법
### 1. 주어진 그래프에서, start 지점이 주어지면 deque(\[start\])를 선언한다. 그리고 방문한 것 노드를 확인하기 위한 visited라는 set()을 선언한다.
### 2. while deque : 로 요소가 있는지 계속 체크한다.
### 3. 요소를 왼쪽에서 하나 꺼내어 node 변수에 저장한다.
### 4. 만약 방문하지 않았다면, visited에 해당 요소를 추가한 후(방문 처리), node를 왼쪽 요소를 꺼내어 업데이트한다. 
### 5. graph에서 해당 node를 key로 하여 방문하지 않은 요소만 추가한다.
### 6. 모두 방문했다면, 더 이상 추가할 것이 없어 while queue가 자연스럽게 빈 상태가 되고 종료가 된다.
### 7. visited를 리턴한다.
### <br/>

### 코드
```
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
```
