class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        stack = []
        for i , bracket in enumerate(s):
            if bracket in opened:
                stack.append(bracket)
                print(stack)
            elif bracket in closed:
                #checking if they are the same type of bracket
                if s[-1] in opened:
                    print(opened.index(s[-1]))
                    if opened.index(stack[-1]) == closed.index(bracket):
                        s.pop()
                    else:
                        return False
        return True
