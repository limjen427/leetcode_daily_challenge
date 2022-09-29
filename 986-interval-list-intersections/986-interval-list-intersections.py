class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i= 0
        j = 0
        
        if (len(firstList) == 0 or len(secondList) == 0):
            return result
        
        while (i < len(firstList) and j < len(secondList)):
            st = max(firstList[i][0], secondList[j][0])
            en = min(firstList[i][1], secondList[j][1])
            
            if (st <= en):
                result.append([st, en])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
            
        return result