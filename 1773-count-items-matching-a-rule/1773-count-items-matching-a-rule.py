class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type':0,'color':1,'name':2} 
        c = 0                            
        index = d[ruleKey]               
        for item in items:                
            if item[index] == ruleValue:  
                c += 1                    
        return c                          