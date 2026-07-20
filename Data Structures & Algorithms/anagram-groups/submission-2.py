class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in keys:
                innerList = keys[key]
                innerList.append(word)
                keys[key] = innerList
            else:
                keys[key] = [word]

        return list(keys.values())



