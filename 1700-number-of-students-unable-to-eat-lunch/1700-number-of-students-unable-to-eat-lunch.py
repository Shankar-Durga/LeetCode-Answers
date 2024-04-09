class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            pop = 0
            for i in range(len(students)):
                if(students[i] == sandwiches[0]):
                    students.pop(i)
                    sandwiches.pop(0)
                    pop = 1
                    break
            if(pop == 0 ):
                break
        return len(students)
                
                    
            