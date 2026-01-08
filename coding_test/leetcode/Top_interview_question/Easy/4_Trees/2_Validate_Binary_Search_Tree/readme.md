### https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
### <br/><br/>

## 풀이
### 1. 왼쪽은 작아야 하고 오른쪽은 커야 하는데, 문제는 상위 노드들 모두에 해당한다.
### 2. 그래서 현재 노드를 비교하고, 최솟값, 최댓값을 지정해줘야 한다. stack에 (node, low, high)을 저장한다.
### 3. 왼쪽이면 low < left.val < val < high가 맞는지 검사한다. 맞으면 stack에 (left, low, val)를 추가한다.
### 4. 오른쪽이면 low < val < left.val < high가 맞는지 검사한다. 맞으면 stack에 (left, val, high)를 추가한다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/218f47e1-6e44-4bb5-9a6a-7d9e4e659f07)
