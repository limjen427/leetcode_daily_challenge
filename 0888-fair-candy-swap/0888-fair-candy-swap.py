class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        # sumAlice, sumBob = sum(aliceSizes), sum(bobSizes)
        # print(sumAlice, sumBob)
        # diff = (sumAlice-sumBob)//2
        # print(diff)
        # for i in aliceSizes:
        #     for j in bobSizes:
        #         if i - diff == j:
        #             print(i, j)
        #             return [i,j]
        A, B = aliceSizes, bobSizes
        dif = (sum(A) - sum(B)) // 2
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]
                    
        