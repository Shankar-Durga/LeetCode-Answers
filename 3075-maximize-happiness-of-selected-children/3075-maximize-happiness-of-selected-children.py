class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = sorted(happiness)
        if(k==1):
            return happiness[-1]
        value = 0
        for i in range(k):
            sample = happiness[-(i+1)]-i
            value = value +( 0 if sample<0 else sample )
        return value
            
        