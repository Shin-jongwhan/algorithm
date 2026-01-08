### https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/553/
### <br/><br/>

## 이해하면 좀 어이 없는 문제
### 아래와 같이 listed node란 리스트이지만 순서가 반영된 리스트이다.
### 그리고 문제는 특정 value가 등장하면 그 value만 삭제하라는 문제다.
#### ![image](https://github.com/user-attachments/assets/cfdf9d8c-5032-4f71-b1e5-e68c8dc2f4d5)
### <br/>

### 먼저 print(node)로 node가 어떻게 생겼는지 보자.
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print(node)
```
### <br/>

### listed node는 다음과 같이 출력된다.
### 전체 node는 \[4,5,1,9\]인데, 없앨 value부터 node가 출력된다.
#### ![image](https://github.com/user-attachments/assets/3b14b3ab-a1ef-4157-8faa-e59e05a1fbe5)
### <br/>

### 그래서 그냥 해당 node를 다음 node로 값을 덮어씌어주면 그럼 자연스럽게 뒤쪽이 당겨와진다.
#### ![image](https://github.com/user-attachments/assets/24c75ed6-eb54-417f-939e-fa4161513ac2)
### <br/>

### 전체 코드
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        print(node)
        node.val = node.next.val
        node.next = node.next.next
```
