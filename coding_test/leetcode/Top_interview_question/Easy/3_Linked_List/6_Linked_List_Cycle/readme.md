### https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/773/
### <br/><br/>

## 첫 번째 시도(answer.py)
### 1. 각 노드의 메모리 주소값을 저장하는 방식을 이용한다. 집합에 저장해서 안에 있는지 비교할 때의 시간복잡도를 최소화한다.
### 2. 만약 같은 메모리 주소가 안에 있으면 return True
### <br/>

### 나쁘지 않다. 
#### ![image](https://github.com/user-attachments/assets/61b7fb9b-b9bd-475e-9970-1e5380b6ae80)
### <br/><br/>

## 최적해 비교(answer_best_score.py)
### 가장 점수가 좋은 코드를 실행해보니 생각보다 안 나오고 비슷하다. 
### 원리는 1칸 씩 참조를 이동하는 slow와 2칸 씩 참조를 이동하는 fast를 활용해서 비교하는 것이다.
### 이게 되게 신기한 게
### 1. fast는 빠르게 이동하니까 None을 만나는 게 훨씬 빠르게 만들 수 있다.
### 2. slow는 1칸씩 이동하므로 모든 경우의 수를 검사할 수 있긴 하다. 하지만 listed node가 길어지면 fast가 slow랑 같아져야 하기 때문에 엄청난 연산을 해야할 수도 있다.
#### ![image](https://github.com/user-attachments/assets/7d1b71ec-13e9-4614-8d53-6e7034e77e99)
