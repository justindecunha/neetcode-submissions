class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for token in tokens:

            match token:
                case "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                case "/":
                    second = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(first / second)
                case "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                case "-":
                    second = int(stack.pop())
                    first = int(stack.pop())
                    stack.append(first - second)
                case _:
                    stack.append(token)
        
        return int(stack.pop())
        