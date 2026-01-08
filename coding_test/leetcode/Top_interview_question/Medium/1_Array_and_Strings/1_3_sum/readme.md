### https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
### <br/><br/>

## 풀이
### 여러가지 방법으로 시도해봤는데 결국 다 타임에러...
### <br/>

### 결국 찾아보았다.
1. nums를 정렬한다.
2. 음수 방향부터인 left와 양수방향부터인 right라는 idx 변수를 만든다.
3. left < right일 때까지 while문을 실행한다. 이 안에서 3 sum이 0보다 크면 right - 1하고, 작으면 left + 1을 한다.
### <br/>

### 시간복잡도
### 위 풀이의 시간복잡도는 (sort) + (for + while) = O( n * log(n) ) + O( n * 1/2n ) = O( n * log(n) ) + O(1/2n^2)로, 차수가 낮은 것과 상수는 무시하고 O(n^2)이 된다.
