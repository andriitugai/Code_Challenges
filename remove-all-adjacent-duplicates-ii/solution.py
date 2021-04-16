class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return s

        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([c, 1])

        # result = ""
        # for e in stack:
        #     result += e[0]*e[1]
        # return result

        result = [e[0] * e[1] for e in stack]
        return "".join(result)
