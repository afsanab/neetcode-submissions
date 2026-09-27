class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack
        stack = []
        for i in tokens:
            # if we have a token that is a num - add to stack
            if i.isnumeric() == True:
                stack.append(int(i))
            # if we have a token that is an operand then
            # pop 2 most recent nums and perform that operation on them
            else:
                y = stack.pop();
                x = stack.pop();
                if i == "+":
                    stack.append(x+y)
                elif i == "-":
                    stack.append(x-y)
                elif i == "*":
                    stack.append(x*y)
                elif i == "/":
                    stack.append(x/y)
        # store result in the stack 
        return int(stack.pop())
                