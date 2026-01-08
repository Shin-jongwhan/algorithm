### https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/631/
### <br/><br/>

## 깊이 균형 이진 탐색 트리(height-balanced binary search tree)
### 1. 왼쪽, 오른쪽 서브 트리의 깊이 차이가 1 이하
### 2. 왼쪽 서브 트리는 노드보다 작은 값만 있고, 오른쪽 서브 트리는 노드보다 큰 값만 있다.
#### ![image](https://github.com/user-attachments/assets/f577514a-6d9e-4bc6-8892-ebca177d
### <br/><br/>

## 풀이
### 일정의 규칙이 있다.
### 리스트는 오름차순으로 정렬되어 있다.
### 먼저 가장 위의 값을 보면 딱 중간 값이다. 그래서 ls\[int(len(ls) - 1)\]의 값이 들어가면 된다.
### 그 다음은 또 반으로 나눈 값이 최상단에 들어간다.
### <br/>

### 여기서 재미있는 트릭이 있다. ls\[:0\] = \[\]이라는 점이다.
### <br/>

### 그래서 재귀함수를 사용하면 된다. 계속 반으로 나누면 된다는 것까지 생각했는데... 구현하는 방법에서 어떻게 중간값을 계속 얻어야 하는지에서 막혀서 결국 찾아보았다.
```
def test(ls) : 
	if ls == [] : 
		return None
	mid = int(len(ls) / 2)
	root = TreeNode(ls[mid])
	root.left = test(ls[:mid])
	root.right = test(ls[mid + 1:])

	return root
```
