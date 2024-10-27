class Solution:
    def sortStack(self,stack):
        tempStack = []
        # ToDo: Write Your Code Here.
        while stack:
            temp = stack.pop()
            while tempStack and tempStack[-1] > temp:
                stack.append(tempStack.pop())
            tempStack.append(temp)
        return tempStack
