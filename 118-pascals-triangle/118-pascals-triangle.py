class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sums = []

        for i in range(numRows):
            sums.append([])
            for j in range(i+1):
                if j == 0 or j == i:
                    sums[i].append(1)
                else:
                    sums[i].append(sums[i-1][j-1] + sums[i-1][j])

        return sums
