class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = inf, inf
        
        for third in nums:
            
            if second < third: return True
            
            if third <= first: first= third    #first세팅
            else:  second = third  #second세팅
                
        return  False