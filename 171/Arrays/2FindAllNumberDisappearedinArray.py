# Given an array nums of n integers where nums[i] is in the range [1, n], 
# return an array of all the integers in the range [1, n] that do not appear in nums.

# Using hashtable 
# O(n) time | O(n)
def findAllNumber1(A):
    table = {}
    for val in A:
        table[val] = 1
    
    ret = []
    for i in range(1, len(A)+1):
        if not i in table:
            ret.append(i)
    return ret

# In-place modification
# O(n) time | O(1) space
def findAllNumber(A):
    for i in range(len(A)):
        # treat the value as a new index 
        new_index = abs(A[i]) - 1
        #print("-->", i, new_index)
        try:
            # make the value negative it is positive 
            if A[new_index] > 0:
                A[new_index] *= -1
        except:
            pass

    #print("A:", A)
    # response array that would contain the missing numbers 
    result = []

    for i in range(1,len(A) + 1):
        if A[i-1] > 0:
            result.append(i)
    #print("returning :", result)
    return result


if __name__ == '__main__':
    A = [4,3,2,7,8,2,3,1] #5,6
    B = [1,1]             #2
    C = [2]               #1

    print(findAllNumber(A))
    print(findAllNumber(B))
    print(findAllNumber(C))
