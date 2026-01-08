class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', ']': '[', '}': '{'}
        opening_brackets = set(bracket_map.values())  # 여는 괄호 집합 생성
        closing_brackets = bracket_map.keys()         # 닫는 괄호 집합

        for char in s:
            if char in opening_brackets:
                stack.append(char)  # 여는 괄호일 경우 스택에 추가
            elif char in closing_brackets:
                if not stack or stack.pop() != bracket_map[char]:  # 짝이 맞지 않으면 False 반환
                    return False
        return not stack  # 스택이 비어 있으면 True, 그렇지 않으면 False