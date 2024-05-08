class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sample = sorted(score,reverse=True)
        a = ["0"]*len(sample)
        
        for i in score:
            data = sample.index(i)
            ans = score.index(i)
            if data+1 == 1:
                a[ans] = "Gold Medal"
            elif data+1 == 2:
                a[ans] = "Silver Medal"
            elif data+1 == 3:
                a[ans] ="Bronze Medal"
            else:
                a[ans] = str(data+1)
        return a
                