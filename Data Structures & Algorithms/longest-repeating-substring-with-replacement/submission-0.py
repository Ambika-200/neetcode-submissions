class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        max_length = 0
        store = {}

        for right in range(len(s)):
            store[s[right]] = store.get(s[right], 0) + 1

            max_count = max(max_count, store[s[right]])

            if (right - left + 1) - max_count > k:
                store[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length