
# Write a function that return true if the given integer is palindrome

# Input = 112112
# Output = False

# Input = 112211
# Output = True 

# Approach 1 : change the number into a list of elements and then use left and right pointer logic 

# Approach 2 : inverse this number to get a new number and check against it 


def palindrome1(input) :
    inputstr = str(input) # A hidden time complexity of rought O(n^2)
    L = len(inputstr)
    left = 0 
    right = L-1

    while left < right:
        if inputstr[left] != inputstr[right]:
            return False
        left += 1
        right -=1
    return True

def palindrome2(input):
    invert = 0
    inputCopy = input 
    counter = 0
    while inputCopy > 0:
        mod = inputCopy % 10  # 998 = 8
        inputCopy //= 10      # 998 = 99
        invert = invert * 10 + mod  # 8, 89
        counter += 1

    #print(input, invert)
    while counter > 0:
        if input % 10 != invert % 10:
            return False
        counter -= 1
        
    return True    
    
A = 112112
B = 112211
print(palindrome1(A))
print(palindrome1(B))
print(palindrome2(A))
print(palindrome2(B))


    