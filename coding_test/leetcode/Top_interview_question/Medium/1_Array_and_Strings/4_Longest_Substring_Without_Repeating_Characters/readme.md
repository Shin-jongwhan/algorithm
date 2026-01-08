### https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
### <br/><br/>

## 풀이
### 중복된 문자가 포함하면 안 되는 조건을 풀려면, dict를 활용하여 푼다.
### key는 char, value는 idx로 한다.
### dict를 검사해서 이미 추가가 되어 있고, substring 영역의 idx이면 idx를 업데이트한다.
### 그게 아니면 substring 길이를 업데이트한다. 
### substring 길이는 i - substring start idx + 1이다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/0333cee5-4cf0-4e0e-bd10-f625748d21f0)
