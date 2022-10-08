class Solution:
    def sortSentence(self, s: str) -> str:
        dict_t = {}
        ans = []
        for word in s.split():
            num = int(word[-1])
            val = word[:-1]
            dict_t[num] = val
        for key in sorted(dict_t.keys()):
            ans.append(dict_t[key])
        return " ".join(ans)