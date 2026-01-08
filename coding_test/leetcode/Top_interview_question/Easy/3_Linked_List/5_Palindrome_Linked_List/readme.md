### https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/772/
### <br/><br/>

## 첫 시도(answer.py)
### 1. palindrome은 앞으로 읽어도 뒤로 읽어도 똑같아서 deque를 활용해서 하나는 그대로, 하나는 거꾸로 넣어줬다.
### 2. 그리고 dq1 == dq2 해서 리턴
### <br/>

### 러닝 타임이 망했다. deque를 쓰면 그래도 insert 하는데에는 얼마 걸리지 않으니까 속도가 괜찮을 거라고 생각했다.
#### ![image](https://github.com/user-attachments/assets/76015cf2-2f75-4ce3-8305-d684640ce1df)
### <br/><br/>

## 두 번째 시도
### 다음을 개선하였다.
### 1. 리스트가 2개까지 필요하지 않다. 리스트가 2배로 감소한 만큼 메모리도 감소하고 연산량도 감소한다. 양쪽이 같이 때문에 하나만 있으면 된다.
### 2. (len(ls) / 2)가 항상 내림인 점을 이용한다. 그러면 홀수 개일 경우 가운데는 무시할 수 있다(palindrome에서 항상 참을 만드는 위치라서 무시 가능함).
### 3. (len(ls) / 2)만큼 for loop을 돌려서 시간복잡도를 감소시킨다.
### <br/>

### 러닝 타임 결과
#### ![image](https://github.com/user-attachments/assets/49a735b7-abaa-452c-9474-93b7b814eae9)
