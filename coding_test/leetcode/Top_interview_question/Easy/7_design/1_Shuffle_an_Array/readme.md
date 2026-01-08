### https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
### <br/><br/>

## 풀이
### 일반적으로 하는 방법은 다음과 같다.
### `코딩 테스트 할 때는 직접 구현하지 말고 아래 방법으로 한다.`
1. for i in range(len(ls) - 1, -1, -1)으로 리스트를 거꾸로 읽어서 0 ~ i 사이에서 랜덤 인덱스 얻음 : random.randint(0, i + 1).
##### * for i in range(len(ls) - 1, -1, -1)로 거꾸로 읽는 이유는 이미 섞인 것은 제외하여 효율적으로 읽게 하기 위함
2. i와 j를 교환한다.
```
lsShuffle[i], lsShuffle[j] = lsShuffle[j], lsShuffle[i]
```
### <br/>

### 랜덤 셔플을 일으키는 원리를 알고 싶어 직접 구현하였다.
### 난수 생성 알고리즘은 메르센 트위스터(Mersenne Twister) 알고리즘이 있고 파이썬에서 널리 채택되고 있다.
### 리스트를 섞는 알고리즘은 Fisher-Yates 알고리즘이라고 하며, Mersenne twister 알고리즘과 같다고 보면 되는데, 그냥 리스트 버전이다.
### 전체적인 과정은 XOR, AND 논리 게이트와 비트 쉬프트를 일으킴으로써 난수를 추출한다.
### 또한 보통 32비트로 한정하기 때문에 2^31 - 1 범위로 난수가 발생된다.
### 한정된 범위(i ~ j)는 i + (rand % (j + 1))를 이용하여 추출한다.
### 랜덤한 것을 계속 적용하고 싶으면 여러가지 방법이 있지만, time.time()과 같이 계속 변하는 수를 넣어줘서 랜덤 seed를 지속적으로 초기화시킨다.
### <br/>

### 러닝 타임
### 직접 구현한 결과도 딱히 나쁘지는 않다.
#### ![image](https://github.com/user-attachments/assets/1863148c-e7ac-409d-85ac-f44fecc0fc4e)
