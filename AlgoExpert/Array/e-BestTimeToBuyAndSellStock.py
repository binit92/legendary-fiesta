
def maxProfit(prices):
    
    minSoFar = float("inf")
    maxDiff = 0
    for i in range(0, len(prices)):
        if prices[i] < minSoFar:
            minSoFar = prices[i]
        else:
            maxDiff = max(maxDiff, prices[i] - minSoFar)
                
    return maxDiff

    
if __name__ == '__main__':
    A = [7,1,4,3,6,4]
    print(maxProfit(A))
                    