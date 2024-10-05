class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]
        for i in range(1,numRows):
            temp = [1]
            for j in range(1,i):
                temp.append(a[i-1][j-1]+a[i-1][j])
            temp.append(1)
            a.append(temp)
        return a