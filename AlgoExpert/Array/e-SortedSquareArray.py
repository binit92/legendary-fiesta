# Write a function that square each element of the sorted list and returns it in ascending order

# A = [1, 2, 3, 5, 6, 8, 9]
# [1, 4, 9, 25, 36, 64, 81]


# Can the input contains -ve values ? 
# A = [-3, -2 , 1]   [1, -2 , -3]
# [1, 4, 9]


# Approach 1  : square each element and apply sorting
# Approach 2 :  use left and right pointers and compare the squared value to keep it at right place

def sortedSquare1(A):
    for i in range(0, len(A)):
        A[i] = A[i] ** 2
    
    A.sort()
    return A

def sortedSquare2(A):
    left = 0 
    right = len(A)-1
    while left < right:
        if abs(A[left]) > abs(A[right]):
            A[left] , A[right] = A[right], A[left]

        left += 1 
        right -= 1
    
    for i in range(0, len(A)):
        A[i] = A[i] ** 2
    return A        

def sortedSquare3(A):
    left = 0
    right = len(A) -1
    while left <= right:
       
        if abs(A[left] > abs(A[right])):
            A[left], A[right] = A[right], A[left]
            A[right] = A[right] ** 2
            right -= 1

        else:
            A[left] = A[left] ** 2
            left += 1
        
    if left == right :
        A[right] = A[right] ** 2

    return A   
        

A = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquare1(A)) # O(n)

A = [1, 2, 3, 5, 6, 8, 9]
print(sortedSquare2(A)) # O(n/2) + O(n)

A = [1, 2, 3, 5, 6, 8]
print(sortedSquare3(A))