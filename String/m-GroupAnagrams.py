words = ["yo", "act", "flop", "tac", "foo", "cat","oy","olfp"] 

# output = [["yo", "oy"], ["flop", "olfp"], ["act","tac","cat"], ["foo"]]


#Approach 
# compare each element to all next element 
# use a helper function to determine anagram 
# determine anagram using hashtable 
# create output list to return in the process

def GroupAnagrams(words):
    ret = []
    
    i = 0
    while i < len(words):
        j = i+1
        localList = []
        localList.append(words[i])
        localTable = createDictionary(words[i])
        #print(words)
        while j < len(words): 
            #print(words)
            if len(words[i]) == len(words[j]):
                newTable = createDictionary(words[j])
                if matchDictionary(localTable,newTable):
                    localList.append(words[j])
                    words.pop(j)
                    j-=1   
            j+=1            
        words.pop(i)
        #i+=1
        #print(localList)
        ret.append(localList)
    return ret

def createDictionary(word):
    table = {}
    for val in word:
        table[val] = table.get(val,0) + 1
    return table
    
def matchDictionary(table1, table2):
    if len(table1) != len(table2):
        return False
    else:
        for key1, val1 in table1.items():
            if key1 in table2:
                if val1 != table2[key1]:
                    return False
            else:
                return False
    return True

print(GroupAnagrams(words))