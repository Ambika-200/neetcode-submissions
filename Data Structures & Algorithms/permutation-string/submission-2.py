class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        s1_count = {}
        window_count = {}

        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        while right < len(s2):
           window_count[s2[right]] = window_count.get(s2[right], 0) + 1

           if right - left + 1 > len(s1):
             window_count[s2[left]] -= 1
             if window_count[s2[left]] == 0:
               del window_count[s2[left]]
             left += 1

           if s1_count == window_count:
             return True
           right += 1
        return False
    
            