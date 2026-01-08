### https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
### <br/><br/>

## 풀이
### 못 풀었다. ㅠ
### 뭔가 간단한데 간단하지 않은 느낌... 
### 결국 찾아보았다.
```
nums = [1,2,3,4,5]		# True
nums = [5,4,3,2,1]		# False
#nums = [2,1,5,0,4,6]		# True
#nums = [20,100,10,12,5,13]		# True

def test() : 
    first, second = 5 * 106, 5 * 106

    for third in nums:
        print(first, second, third)
        if second < third: return True
        
        if third <= first: first = third    #first세팅
        else:  second = third  #second세팅
            
    return  False


test()
```
