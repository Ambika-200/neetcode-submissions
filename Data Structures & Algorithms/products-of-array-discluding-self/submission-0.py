class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[]
        prefix=1
        for i in range(len(nums)):
            store=prefix
            result.append(store)
            prefix=prefix*nums[i]
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            result[i]=result[i]*postfix
            postfix=postfix*nums[i]
        return result
           
            
            
         
          