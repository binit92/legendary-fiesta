# https://leetcode.com/problems/subsets-ii/

# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

 
# O(n * 2^n) time | O(n * 2^n) space


def subset(nums):
    ret = []
    nums.sort()
    
    def backtrack(i,subset):
        if i == len(nums):
            ret.append(subset[::])
            return
        
        # All subset that include nums[i]
        subset.append(nums[i])
        backtrack(i + 1, subset)
        
        # All subset that doesn't include nums[i]
        subset.pop()
        
        # skip i when nums are equal ? 
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        backtrack(i + 1, subset)
        
    backtrack(0,[])
    return ret

if __name__ == '__main__':
    nums = [1,2,2]  #[[],[1],[1,2],[1,2,2],[2],[2,2]]
    print(subset(nums))