class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        longest_prefix = ""

        for i in range(len(first_word)):
            character = first_word[i]

            for item in strs:
                if len(item) <= i or item[i] != character:
                    return longest_prefix
                
            longest_prefix += character

        return longest_prefix