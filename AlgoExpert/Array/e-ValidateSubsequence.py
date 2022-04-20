# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# 
# output = true
# 
# 
# Approach
#  take two pointers and match,
#  if matched increment both pointers 
#  otherwise increment only the pointer of array
#  At END : if all the elements in sequence is traversed, it is valid subsequence
# 
def validatesubsequence(array, sequence):
    if len(array) < len(sequence):
        return False
    i = 0 
    j = 0
    
    while i < len(array):
        if array[i] == sequence[j]:
            j += 1        
        i+= 1
    #print(i,j)   
    return j == len(sequence) 
    

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(validatesubsequence(array, sequence))
    
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 11]    
print(validatesubsequence(array, sequence))
