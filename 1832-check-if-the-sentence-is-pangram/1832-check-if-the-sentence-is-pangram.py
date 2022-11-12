class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = set(sentence)
        return len(check) == 26