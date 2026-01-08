### https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
### <br/><br/>

## 풀이
### 나는 모든 palindromic seqeuce를 만나면 구해서 저장한 결과보다 길이가 길면 업데이트하는 방식으로 하였다.
### 홀수, 짝수 형식으로 나눴다.
- 문자열을 처음부터 끝까지 for loop으로 하나씩 읽는다.
- 홀수 / 짝수 형태를 구분한다.
- 홀수 : i, i - 2와 같은지 검사한다.
- 짝수 : i, i - 1이 같은지 검사한다.
- 진행하면서 만나면 palindrom의 길이를 구한다.
- 만약 저장된 길이보다 최근 발견한 것이 길면 긴 것으로 업데이트한다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/323ce94f-d243-4224-9b88-a7b7c31d29f8)
### <br/>

### best score 코드
### 찾아보니 모든 palindromic seqeunce를 구하는 게 아니라, 가장 긴 것을 구하면, 그 길이를 저장하고, 그 길이보다 큰 것들만 필터링해서 찾았다.
