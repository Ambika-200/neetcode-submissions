class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store={}
        for i in range(len(nums)):
            if nums[i] not in store:
               store[nums[i]]= 1        
            else:
               store[nums[i]] += 1    
        numbers=sorted(store, key=store.get, reverse=True)
 
        return numbers[:k]

  