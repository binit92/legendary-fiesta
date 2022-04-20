# https://leetcode.com/problems/letter-case-permutation

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create. Return the output in any order.

# 4 Approach 
# Iteration
# Recursion
# Binary Mask 
# Built-in library Function

# Iterative Approach
# O(n * 2^n) time | O(n * 2^n) space (how ?), where n is number of character in s
def letterCasePermutation(s):
    output = [""]
    for val in s:
        ret = []
        for o in output:
            if val.isalpha():
                ret.append(o + val.upper())
                ret.append(o + val.lower())
            else:
                ret.append(o + val)
        output = ret
    return output

if __name__ == '__main__':
    s = "a1b2" #["a1b2","a1B2","A1b2","A1B2"]
    print(letterCasePermutation(s))
