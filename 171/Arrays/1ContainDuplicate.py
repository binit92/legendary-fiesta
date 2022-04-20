

# O(n^2) time | O(1) space
# O(nlogn) | O(n) or O(logn) space - Python uses Timsort() that has a worst space complexity as O(n)
# O(n) | O(n) space

def containsDuplicate(nums):
        table = {}
        for val in nums:
            if val in table:
                return True
            else:
                table[val] = True
        return False

if __name__ == "__main__":
    A = [1,2,3,4]
    print(containsDuplicate(A))