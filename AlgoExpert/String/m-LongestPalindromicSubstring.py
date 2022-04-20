# TODO: solve it in O(n^2) time 

# Write a function that given a string returns its longest palindromic substring 

string = "abaxyzzyxf"
# output: "xyzzyx"

# Approach : Brute force 
# # starting from left and right pointer, check if those matches, if yes, check for palindrome 

# O(n^3) time | O(n) space
def longestPalindromicSubstring(A):

    longest = 0
    longestStr = ""
    for i in range(0, len(A)-1):
        for j in reversed(range( i+1 , len(A))):
            if A[i] == A[j]:
                substring = A[i:j+1]
                #print(substring)
                if isPalindrome(substring):
                    length = len(substring)
                    if length > longest:
                        longest = length
                        longestStr = substring
                        break
    
    #print("longest : ", longest  )
    #print("str: ", longestStr)
    return longestStr

# helper function
def isPalindrome(A):
    left = 0 
    right = len(A)-1
    while left < right:
        if A[left] == A[right]:
            left+=1
            right-=1
        else:
            return False

    return True

print(longestPalindromicSubstring(string))