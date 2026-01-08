### https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/627/
### <br/><br/>

## 풀이
### 거울상인지 검사하는 문제
### 거울상이려면 무조건 처음 node의 왼쪽 오른쪽부터 같아야 한다. 
### 그래서 2번째 depth의 왼쪽 node, 오른쪽 node로 나눈다. stack에 (left_node, right_node)형식으로 저장한다.
### 그 다음 존재하는지와 값이 모두 동일하면 계속 넘어가고, 아니라면 return False
### 1. 먼저 root가 비었는지, [1]과 같이 1 depth만 있는지, [1,2,None], [1,None,2]와 같이 2 depth가 맞지 않은지는 미리 검사한다.
### 2. 그리고 거울상은 left.left == right.right, left.right == right.left이어야 한다. 
### 3. 만약 둘 다 None이면 일단 다음 검사를 위해 pass
### 4. 만약 1, 2가 아니면 return False
#### <br/>

### 러닝 타임
### 조건문을 적절하게 잘 써서 그런지 잘 나왔다.
#### ![image](https://github.com/user-attachments/assets/0a229f03-55bb-4c6b-928e-bebfaca3d4d3)
