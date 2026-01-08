### https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
### <br/><br/>

## 풀이
### 1. stack을 이용한다. 그런데 각 node에서 depth를 계산해야 하므로 stack에 depth를 같이 저장한다. max_depth = 0으로, stack = \[(root, 1)\]로 초기화한다.
### 2. stack에서 pop()을 이용하여 값을 하나씩 빼서 node, depth에 각각 저장한다.
### 3. max_depth = max(max_depth, depth)
### 4. 만약 tree에서 left, right 각각이 None이 아니면 stack에 추가한다.
#### ![image](https://github.com/user-attachments/assets/c5708154-50d1-4d50-a83d-ab0829d0ce91)
