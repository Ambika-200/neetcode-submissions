class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = {}
        window = {}
        left = 0
        right = 0
        min_len = float("inf")
        start = 0

        for char in t:
            required[char] = required.get(char, 0) + 1

        need = len(required)
        have = 0

        while right < len(s):
            window[s[right]] = window.get(s[right], 0) + 1

            if s[right] in required and window[s[right]] == required[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                char = s[left]
                window[char] -= 1

                if char in required and window[char] < required[char]:
                    have -= 1

                left += 1

            right += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]
