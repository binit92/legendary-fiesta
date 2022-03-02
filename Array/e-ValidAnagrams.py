class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        table = {}
        for val in s:
            table[val] = table.get(val,0) + 1
        for val in t: 
            if val in table:
                if table[val] < 0:
                    return False
                else:
                    table[val] = table[val]-1
            else:
                return False
            
        for key,val in table.items():
            if val >0:
                return False
            
        return True

# anagram nagram
# cat car        