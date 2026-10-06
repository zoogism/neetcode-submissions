class Solution:
    def calPoints(self, operations: List[str]) -> int:

        x = []
        total_sum = 0

        for i in range(len(operations)):
            if operations[i] == '+':
                x.append(x[-1] + x[-2]) # utulised peek here 

            elif operations[i] == 'D': # utulised peek here 
                x.append(x[-1] * 2)
            
            elif operations[i] == 'C':
                x.pop() # utulised pop here
            else:
                x.append(int(operations[i]))  # utulised push here
            
            
        
        return sum(x)
            

        

        