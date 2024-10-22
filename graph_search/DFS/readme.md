# DFS
### 재귀함수 버전이 있고, stack 버전이 있는데 나는 stack 버전이 마음에 든다.
#### ![image](https://github.com/user-attachments/assets/6097fcdf-cfde-4b59-9e22-d96c665dbce2)
### <br/><br/><br/>


## 구현 
### 1. start를 stack이라는 리스트에 먼저 넣는다. 그리고 visited라는 집합을 만든다. 
### 집합은 중복을 허용 안 하기 때문에 유용하고, 어떤 값이 있는지 검사하는 데에 시간복잡도는 O(1)이다.
#### * 그런데 먼저 graph가 node가 없는지 검사한 후 node가 아무 것도 없다면 그냥 리턴한다.
### 2. while stack : 으로 stack이 있는지 검사한다.
### 3. node라는 변수에 stack.pop()을 하여 가장 오른쪽 값을 저장한다.
### 4. 만약 node를 방문하지 않았다면 visited.add(node)로 방문 처리하고 방문한 node를 output에 저장하거나 출력한다. 왜냐면 set은 순서가 없기 때문에 우리가 예상하는 결과와 다르게 나오기 때문이다.
### 5. reversed(graph\[node\])로 for loop을 돌면서 해당 값이 방문하지 않았다면, stack에 추가한다.
### reversed로 하는 이유는 stack.pop()을 할 때에 오른쪽부터 꺼내는데, 오른쪽이 가장 먼저 연결된 node여야 하기 때문이다.
