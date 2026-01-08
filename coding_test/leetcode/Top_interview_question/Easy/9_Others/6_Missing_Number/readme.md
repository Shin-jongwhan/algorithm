### https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/722/
### <br/><br/>

## 풀이
### set을 이용하여 정해진 값 범위에서 없는 것을 return 하였다.
### nums에 포함된 숫자는 항상 0부터 시작, 그리고 마지막 숫자를 항상 포함한다.
### <br/>

### 러닝 타임
#### ![image](https://github.com/user-attachments/assets/7769992a-2b10-4640-b0ce-84c3599a612e)
### <br/>

### best score answer는 수학적으로 간단하게 풀었다.
```
# len(nums) * (len(nums) + 1) // 2 : 0 ~ n 만큼의 합
# sum(nums) : missing num을 제외한 합
# 결과적으로 (0 ~ n 만큼의 합) - (missing num을 제외한 합) = missing num
len(nums) * (len(nums) + 1) // 2 - sum(nums)
```
