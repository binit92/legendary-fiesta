# Min Max Stack Construction
# Write a MinMaxStack class for a Min Max Stack. The class should support:
# + Pushing and popping values on and off the stack
# + Peeking at the value at the top of the stack.
# + Getting both the minimum and the maximum values in the stack at any give point in time 

class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]

    # O(1) time | O(1) space 
    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    # O(1) time | O(1) space 
    def push(self, number):
        newMinMax = {"min" : number, "max" : number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["min"]

    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) -1]["max"]

if __name__ == '__main__':
    stack = MinMaxStack()
    stack.push(10)
    stack.push(11)
    stack.push(13)
    stack.push(14)
    print(stack.getMin() , " ", stack.getMax())
    stack.pop()
    print(stack.getMin() , " ", stack.getMax())
