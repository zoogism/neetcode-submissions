class Solution:
    def calPoints(self, operations: List[str]) -> int:

        x = []
        total_sum = 0

        for i in range(len(operations)):
            if operations[i] == '+' and len(x) > 1:
                
                x.append(x[-1] + x[-2])

            elif operations[i] == 'D':
                x.append(x[-1] * 2)
            
            elif operations[i] == 'C':
                x.pop()
            else:
                x.append(int(operations[i]))
            
            
        
        return sum(x)
            

        

        