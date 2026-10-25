class Solution:

    def encode(self, strs: List[str]) -> str:
        resulting_string = ""
        encoding_character = "~" # The character which will separate strings

        for item in strs:
            resulting_string += str(len(item)) + encoding_character + item
        
        return resulting_string



    def decode(self, s: str) -> List[str]:

        words = []
        position = 0

        while position < len(s):
            separator = s.index("~",position)

            length = int(s[position:separator])

            start = separator + 1
            end = start + length

            words.append(s[start:end])

            position = end

        return words
