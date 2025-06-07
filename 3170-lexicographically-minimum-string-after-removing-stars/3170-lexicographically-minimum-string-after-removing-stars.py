class Solution:
    def clearStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                # Find and remove the smallest character in the stack
                if stack:
                    # Find the index of the smallest character
                    min_char = min(stack)
                    min_idx = stack.index(min_char)
                    # Remove the smallest character
                    stack.pop(min_idx)
            else:
                stack.append(char)
        
        return ''.join(stack)