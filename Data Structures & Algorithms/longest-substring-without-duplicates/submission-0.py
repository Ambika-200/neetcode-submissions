class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count=0
        left=0
        right=0
        store={}
        while right < len(s): 
            if s[right] in store:
                 left = max(left, store[s[right]] + 1)
            store[s[right]] = right 
            max_count = max(max_count, right - left + 1)
            right += 1
        return max_count
            
             


        