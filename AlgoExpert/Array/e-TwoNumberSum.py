
# three approaches to solve this question
# 1. two loops 
# 2. sort and use left and right pointers
# 3. use a hashtable 

# input 
# A = [1, 12, 3, 2, 8, 6, 3 , 5]
# target = 10
# output 
# [2, 8]

# O(n^2) time | O(1) space
def two_sum1(A, target):
    for i in range (0, len(A) -1 ):
        for j in range(i, len(A)):
            if A[i] + A[j] == target:
                return [A[i], A[j]]
    return -1

# O(n) time | O(1) space
def two_sum2(A,target):
    # sorted and sort() 
    A.sort()  # sort() is in-place sorting .. so no extra space
    i = 0
    j = len(A) - 1

    while i < j:
        if A[i] + A[j] == target:
            return [A[i], A[j]]
        elif A[i] + A[j] < target:
            i+=1 
        else:
            j-=1

    return -1

# O(n) time | O(n) space 
def two_sum3(A, target):
    H = {}
    for val in A: 
        if target - val in H:
            return [val, target-val]
        else:
            H[val] = 1
    return -1 

A = [1, 12, 3, 2, 8, 6, 3 , 5]
target = 10
print(two_sum1(A,target))
print(two_sum2(A,target))
print(two_sum3(A,target))
