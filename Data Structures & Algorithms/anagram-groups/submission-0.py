class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}

        for i in range(len(strs)):
            word = strs[i]
            key = ''.join(sorted(word))

            if key not in store:
                store[key] = []

            store[key].append(word)

        return list(store.values())