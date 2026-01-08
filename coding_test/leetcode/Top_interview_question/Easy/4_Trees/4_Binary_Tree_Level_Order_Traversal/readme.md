### https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/628/
### <br/><br/>

## 풀이
### 깊이에 따라 리스트를 만드는 문제
```
# 1층
[[1]]

# 2층
[[1], [2,3]]

# 3층
[[1], [2,3], [4,5]]
```
### <br/>

### tree 문제는 stack을 활용하면 참 좋다.
### 1. stack에 (node, depth)를 저장하는데 왼쪽부터 오른쪽 순서로 저장한다. popleft로 하나씩 꺼낸다.
### 2. node.left, node.right가 각각 있으면 (다음 node, depth + 1)을 stack에 저장한다. 
### 3. 만약 depth가 같다면 ls\[-1\].append(node.val), 같지 않다면 ls.append(\[node.val\])을 한다. 
#### 그런데 '같지 않다면'은 사실 정확한 건 아니고 len(ls) + 1 == depth로 검사하긴 해야 하는데, 로직상 '반드시' 이 상태를 검사하기 때문에 상관 없다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/e2daaf1f-a0ab-4a0d-add9-2c76c389b5c3)
