class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []

        def collections_val(i, cur, total):

            if total == target:
                combination.append(cur.copy())
                return 
            if total > target or i>=len(candidates):
                return
           
            cur.append(candidates[i]) 
            collections_val(i, cur,total+candidates[i])  
            cur.pop()
            collections_val(i+1, cur, total) 

        collections_val(0,[],0)    
        return combination

