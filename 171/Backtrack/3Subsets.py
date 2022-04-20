# https://leetcode.com/problems/subsets/

# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# 4 Approach
# Cascading 
# Backtracking 
# Lexicographic (Binary Sorted) Subsets
# DFS

# Cascading (Iterative) Solution
# O(n * 2^n) time | O(n * 2^n) space, where n is number of element in nums
def createSubsets(nums):
    output = [[]]
    for val in nums:
        ret = []
        for o in output:
            ret.append(o + [val])
            ret.append(o)
        output = ret
    return output

# DFS - backtracking 
def createSubsets2(nums):
    ret = []

    subset = []
    def dfs(i):
        # base case 
        if i == len(nums):
            # copying the subset because we don't want to overwrite it 
            ret.append(subset[::])
            return

        # include the new character
        subset.append(nums[i])
        dfs(i+1)

        # NOT include the new character
        subset.pop()
        dfs(i+1)

    dfs(0)
    return ret

if __name__ == '__main__':
    nums = [1,2,3] # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(createSubsets(nums))
    print(createSubsets2(nums))