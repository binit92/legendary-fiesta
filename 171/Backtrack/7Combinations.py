
# TODO : What is the time complexity of this ? 
# TODO : What are the alternate approaches ? 

def combination(n,k):
    results = []
    for i in range(1,n+1):
        backtrack(n,k,i+1,[i],results)
    return results

def backtrack(n,k, idx, curr, results):
    if len(curr) == k:
        results.append(curr)
        return

    for i in range(idx, n+1):
        backtrack(n,k, i+1, curr + [i], results)


if __name__ == "__main__":
    n = 4
    k = 2
    print(combination(n,k))