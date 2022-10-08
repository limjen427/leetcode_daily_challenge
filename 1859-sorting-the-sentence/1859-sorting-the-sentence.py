class Solution:
    def sortSentence(self, s: str) -> str:
        dic = {}
        result = []
        for word in s.split():
            num = int(word[-1])
            val = word[:-1]
            dic[num] = val
        for key in sorted(dic.keys()):
            result.append(dic[key])
        return " ".join(result)