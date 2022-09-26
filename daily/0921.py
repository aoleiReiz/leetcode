from typing import Optional
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        p = dummy_head
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy_head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        while p and p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0 or len(mat[0]) == 0:
            return 0
        ans = 0
        for i in range(m):
            ans += mat[i][i]
        for i in range(m):
            j = m - 1 - i
            if i == j:
                continue
            ans += mat[i][j]
        return ans

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat
        idx = 0
        ans = []
        temp = []
        while idx < m * n:
            if len(temp) == c:
                ans.append(temp)
                temp = []
            orig_row = idx // n
            orig_col = idx % n
            temp.append(mat[orig_row][orig_col])
            idx += 1
        ans.append(temp)
        return ans

    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1 = 0
        idx2 = 0
        letters = []
        sign = True
        while idx1 < len(word1) and idx2 < len(word2):
            if sign:
                letters.append(word1[idx1])
                idx1 += 1
                sign = False
            else:
                letters.append(word2[idx2])
                idx2 += 1
                sign = True
        while idx1 < len(word1):
            letters.append(word1[idx1])
            idx1 += 1
        while idx2 < len(word2):
            letters.append(word2[idx2])
            idx2 += 1
        return "".join(letters)

    def interpret(self, command: str) -> str:
        idx = 0
        ans = []
        while idx < len(command):
            if command[idx: idx + 1] == "G":
                ans.append("G")
                idx += 1
            elif command[idx: idx + 2] == "()":
                ans.append("o")
                idx += 2
            elif command[idx: idx + 4] == "(al)":
                ans.append("al")
                idx += 4
        return "".join(ans)

    def findTheDifference(self, s: str, t: str) -> str:
        letter_count = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}
        for c in t:
            letter_count[c] += 1
        for c in s:
            letter_count[c] -= 1
        for c in letter_count:
            if letter_count[c] == 1:
                return c
        return ""

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        q = [(sr, sc)]
        seen = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        orig_color = image[sr][sc]
        while q:
            temp = []
            for point in q:
                i, j = point
                image[i][j] = color
                seen[i][j] = True
                for direction in directions:
                    new_i = i + direction[0]
                    new_j = j + direction[1]
                    if (0 <= new_i < m and 0 <= new_j < n) and not seen[new_i][new_j] and image[new_i][new_j] == orig_color:
                        temp.append((new_i, new_j))
            q = temp
        return image

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ans = 0
        for i in range(m):
            for j in range(n):
                if seen[i][j] or grid[i][j] == 0:
                    continue
                else:
                    #bfs
                    q = [(i, j)]
                    cur = 0
                    seen[i][j] = True
                    while q:
                        temp = []
                        for point in q:
                            i, j = point
                            cur += 1
                            for direction in directions:
                                new_i = i + direction[0]
                                new_j = j + direction[1]
                                if (0 <= new_i < m and 0 <= new_j < n) and not seen[new_i][new_j] and grid[new_i][
                                    new_j] == 1:
                                    seen[new_i][new_j] = True
                                    temp.append((new_i, new_j))
                        q = temp
                    ans = max(ans, cur)
        return ans

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node

if __name__ == '__main__':
    s = Solution()
    ma = s.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    print(ma)
