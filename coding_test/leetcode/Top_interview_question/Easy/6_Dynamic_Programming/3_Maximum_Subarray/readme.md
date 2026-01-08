### https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/566/
### <br/><br/>

## 풀이
### 여기서 나오는 dynamic programming 파트가 대부분 수학 문제인데, 내가 수학 문제에 약하다는 걸 느낀다.
### 잘 안 풀려서 결국 또 best score인 코드를 봤다.
#### 아래 코드를 봐도 사실 바로 이해가 되지 않았다. 하지만 몇 개 예시를 풀어보니, 이 코드가 어떻게 maximum sum을 구할 수 있는지 이해가 됐다.
#### 숫자는 음수도 있고 양수도 있다(0은 무시). 모두 음수일 가능성도 있다.
#### 이런 저런 가능성을 생각해봤었는데, 이 코드에서는 모두 음수일 때도 항상 최댓값을 찾아주었다.
#### 그리고 다른 의문점은, 중간에 큰 수가 있다면 어떻게 되는가 하는 거였는데 테스트를 몇 개 해보니 그러한 점은 고려할 수 있다는 걸 알 수 있었다.
```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        current_sum = 0
        
        for num in nums:
            current_sum += num
            if current_sum > max_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        
        return max_sum
```
