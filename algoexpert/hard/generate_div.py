from typing import List

def generateDivTags(numberOfTags):
    # Write your code here.
    ans = []
    def backtrack(s, left, right):
        if len(s) == 2 * numberOfTags:
            ans.append("".join(s))
            return
        if left < numberOfTags:
            s.append("<div>")
            backtrack(s, left + 1, right)
            s.pop()
        if right < left:
            s.append("</div>")
            backtrack(s, left, right + 1)
            s.pop()
    backtrack([], 0, 0)
    return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('<div>')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append('</div>')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans


print(generateDivTags(3))

print(Solution().generateParenthesis(3))