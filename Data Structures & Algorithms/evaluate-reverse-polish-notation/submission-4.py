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
            elif len(stack) >= 2:
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
        if len(stack) >= 1:
            return int(stack.pop())
        else:
            return 0
        
                