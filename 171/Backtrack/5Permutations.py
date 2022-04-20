# TODO : What is the time complexity of this ? 
# TODO : What are the alternative approaches to solve this ? 
# 

def permutations(nums):
    results = []
    seen = set()
    for i in range(len(nums)):
        seen.add(nums[i])
        backtrack(nums, i, seen, [nums[i]], results)
        seen.remove(nums[i])
    return results

def backtrack(nums,idx, seen, curr, results):
    if len(curr) == len(nums):
        results.append(curr)
        return

    for i in range(len(nums)):
        if i == idx or nums[i] in seen:
            continue
        seen.add(nums[i])
        backtrack(nums,i, seen, curr + [nums[i]], results)
        seen.remove(nums[i])

if __name__ == '__main__':
    nums = [1,2,3]
    print(permutations(nums))