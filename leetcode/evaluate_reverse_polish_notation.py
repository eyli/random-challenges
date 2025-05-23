# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        token_stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                token_stack.append(int(token))
            else:
                right = token_stack.pop()
                left = token_stack.pop()
                if token == '+':
                    token_stack.append(left + right)
                elif token == '-':
                    token_stack.append(left - right)
                elif token == '*':
                    token_stack.append(left * right)
                elif token == '/':
                    token_stack.append(int(left / right))
        return token_stack.pop()
