### https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/
### <br/><br/>

## 주의할 점
### 문제를 풀면서 새로운 걸 배웠다.
### 자세한 건 test.ipynb을 참고하자.
### 클래스를 변수로 참조할 때는 다음과 같은 특징이 있다.
### <br/>

### 1. 다음은 값을 바꾸지는 못 한다. 다음 node로 이동만 한다.
```
current = node
current = current.next
```
### <br/>

### 2. 함수 안에서, 다음은 값을 바꿀 수 있다.
```
current = node
return current.next
```
### <br/>

### 3. 1번의 특성으로 인해 값을 바꾸려면 아래와 같이 해야 하는데, 맨 마지막 값이 None이기 때문에 에러가 난다.
#### ls = \[1,5,9\]의 linked node 출력값
```
1 -> 5 -> 9 -> None
```
#### 값을 바꾸기 위한 값 할당(맨 마지막이 None이기 때문에 에러 날 수 있음)
```
current.next = current.next.next
```
### <br/>

### 하여 다음과 같이 처리하는 게 안전하다.
```
n = 0 
while current : 
	n += 1 
	if n == idx :
		prev.next = prev.next.next
		break
	prev = current
	current = current.next

return node
```
### <br/>

### 4. 아래 둘은 다른 것이다. if node가 검사 범위가 좀 더 넓다. falsy함을 검사한다.
```
if node != None :
if node : 
```
