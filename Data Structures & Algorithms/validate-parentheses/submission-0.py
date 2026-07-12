class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { ")" : "(", "}" : "{", "]" : "["}
        for char in s:
            if char in mapping:
                popped_char = stack.pop() if stack else "#"
                if mapping[char] != popped_char:
                    return False
            else:
                stack.append(char)

        return not stack