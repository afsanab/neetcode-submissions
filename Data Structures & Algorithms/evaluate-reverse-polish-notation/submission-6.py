class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create a stack
        stack = []
        for i in tokens:
            # if we have a token that is a num - add to stack
            if i.lstrip("-").isdigit():
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
                    stack.append(int(x/y))
        # store result in the stack 
        return stack.pop()


    # my mistake here is that i dont always end the code when the stack is empty - i am looping 
        
                