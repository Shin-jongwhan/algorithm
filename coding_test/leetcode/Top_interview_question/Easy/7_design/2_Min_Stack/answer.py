class MinStack(object):
    def __init__(self) : 
        self.min_stack = []
        self.dqMin = deque([])


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min_stack.append(val)
        #if self.min != None : 
        #	self.min_second = self.min
        #if self.min == None or self.min > val : 
        #	self.min = val

        if not self.dqMin : 
            self.dqMin.append(val)
        else : 
            if self.dqMin[-1] >= val : 
                self.dqMin.append(val)
            else : 
                self.dqMin.appendleft(val)


    def pop(self):
        """
        :rtype: None
        """
        if len(self.min_stack) == 0:
            raise IndexError("pop from empty list")
        # 마지막 요소 저장
        last_item = self.min_stack[-1]
        del self.min_stack[-1]

        if last_item == self.dqMin[-1] : 
            self.dqMin.pop()

        # 리스트에서 마지막 요소 반환
        return last_item


    def top(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.dqMin[-1]

    
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()