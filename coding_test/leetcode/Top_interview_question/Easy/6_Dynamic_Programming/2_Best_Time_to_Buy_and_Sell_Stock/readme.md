### https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
### <br/><br/>

## 풀이
### 나는 이 간단한 문제가 이해가 잘 안 됐고, 결국 찾아보았다. 고점과 저점을 찾아야 한다는 생각에 빠져 있었다. 그리고 거기서 저점의 시간이 고점보다 이전 시간이어야 한다는 점... 너무 복잡하게 생각하고 있었다.
### 그런데 그냥 현재 가격에서 찾은 low를 뺀다면 그게 가장 높은 profit이었다. 현재 가격은 항상 low의 시점에서 시간이 지난 시점이니까 가능한 것이다.
### <br/>

### low는 계속 낮아지면 업데이트한다. 
### 그리고 현재 가격 - low가 더 높다면 profit을 업데이트한다.
