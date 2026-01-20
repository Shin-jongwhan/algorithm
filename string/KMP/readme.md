# KMP(Knuth–Morris–Pratt)
### 문자열에서 특정 패턴이 어디에 등장하는지 빠르게 찾는 알고리즘
### 참고
- https://bowbowbow.tistory.com/6
  - 2016년 블로그 글인데 잘 설명해준다.
### <br/>

### 시간복잡도
- LPS 구축: O(m) (m = 패턴 길이)
- 검색: O(n) (n = 텍스트 길이)
- 전체: O(n + m)
### <br/>

### pi (lps)
#### <img width="684" height="710" alt="image" src="https://github.com/user-attachments/assets/6af88989-b657-4720-b5d0-491556f3aa0f" />
#### <br/>

### KMP의 핵심 원리. prefix = suffix 라면, suffix 시작하는 쪽으로 인덱스를 점프하여 이동할 수 있다. 그러면 그게 다시 prefix가 된다.
#### <img width="872" height="737" alt="image" src="https://github.com/user-attachments/assets/b5c9930c-7841-4487-8623-89448abc0290" />
### <br/>

