### https://leetcode.com/explore/interview/card/top-interview-questions-easy/96/sorting-and-searching/774/
### <br/><br/>

## 풀이
### bad 보다 같거나 크면 True, 작으면 False이다.
### 목표 지점을 어떻게 빠르게 찾아가는가에 대한 문제이다.
### 나는 1/2 지점 씩 이동하여 찾았다.
### 절반 위치 i 에서 True이고 i - 1에서 False이면 return i, 아니면 왼쪽으로 남은 크기 만큼의 절반을 이동한다.
### 절반 위치 i 에서 False이고 i + 1에서 True이면 return i + 1, 아니면 오른쪽으로 남은 크기 만큼의 절반을 이동한다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/7c31389c-c58e-46d4-8e6c-fb7cdb8aa1a5)


