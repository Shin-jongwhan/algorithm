### https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/601/
### <br/><br/>

## 풀이
### 규칙을 가장 단순한 것부터 해보면 간단하게 도출할 수 있다.
1. 각 행의 처음과 마지막은 항상 1이다.
```
ls[row][0] = 1
ls[row][-1] = 1
```
2. 그 중간의 수의 위치를 idx로 하면 바로 이전 행의 (idx - 1) + idx이다.
```
ls[row][j] = ls[row-1][j-1] + ls[row-1][j]
```
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/08b5a0a8-f358-4074-a80c-db7dfecca450)
### <br/>

### 파스칼 삼각형은 이항계수의 패턴과 일치한다고 한다는 내용을 보았다.
#### https://www.youtube.com/watch?v=sVq2crKazJI
#### ![image](https://github.com/user-attachments/assets/27fd4144-eec5-418e-be24-b9786f5adbd5)
