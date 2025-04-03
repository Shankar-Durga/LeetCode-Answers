class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        visited = [0]*numCourses
        for i in prerequisites:
            prereq[i[0]].append(i[1])

        def checker(course):
            visited[course] = 2
            
            for i in prereq[course]:
                
                if visited[i] == 2:
                    return True
                if visited[i]==0 and checker(i):
                    return True
            visited[course] = 1
            return False 

        

        for i in prerequisites:
            if checker(i[0]):
                return False
        return True
        
        
        