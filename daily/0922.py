from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        idx_mapping = {num: i for i, num in enumerate(arr)}
        for li in pieces:
            prev_idx = -1
            for num in li:
                if num not in idx_mapping:
                    return False
                idx = idx_mapping[num]
                if idx < prev_idx or (prev_idx != -1 and idx - prev_idx != 1):
                    return False
                else:
                    prev_idx = idx
        return True

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {"(", "[", "{"}:
                stack.append(c)
            else:
                if stack:
                    l = stack.pop()
                    if l == "(" and c != ")":
                        return False
                    elif l == "[" and c != "]":
                        return False
                    elif l == "{" and c != "}":
                        return False
                else:
                    return False
        return len(stack) == 0

    def freqAlphabets(self, s: str) -> str:
        letters_mapping = {(str(i) if i <= 9 else f"{i}#"): c for i, c in enumerate("abcdefghijklmnopqrstuvwxyz", 1)}
        i = len(s) - 1
        ans = []
        while i >= 0:
            if s[i] == "#":
                ans.append(letters_mapping[s[i-2: i+ 1]])
                i -= 3
            else:
                ans.append(letters_mapping[s[i]])
                i -= 1
        return "".join(ans[::-1])

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_mapping = {c: i for i, c in enumerate(order)}
        prev_word = words[0]
        for word in words[1:]:
            i = 0
            j = 0
            while i < len(prev_word) and j < len(word):
                if idx_mapping[prev_word[i]] > idx_mapping[word[j]]:
                    return False
                elif idx_mapping[prev_word[i]] < idx_mapping[word[j]]:
                    break
                else:
                    i += 1
                    j += 1
            if j == len(word) and i != len(prev_word):
                return False
            else:
                prev_word = word

        return True

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        steps_mat = [[0 for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    seen[i][j] = True
                    q.append((i,j))
        step = 0
        while q:
            temp = []
            step += 1
            for point in q:
                i, j = point
                for d in directions:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if 0 <= new_i < m and 0<= new_j < n and mat[new_i][new_j] == 1 and not seen[new_i][new_j]:
                        steps_mat[new_i][new_j] = step
                        seen[new_i][new_j] = True
                        temp.append((new_i, new_j))
            q = temp
        return steps_mat

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = [[False for _ in range(n)] for _ in range(m)]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = []
        fresh_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    seen[i][j] = True
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        step = 0
        while q:
            temp = []
            flag = False
            for point in q:
                i, j = point
                for d in directions:
                    new_i = i + d[0]
                    new_j = j + d[1]
                    if 0 <= new_i < m and 0<= new_j < n and grid[new_i][new_j] == 1 and not seen[new_i][new_j]:
                        flag = True
                        seen[new_i][new_j] = True
                        grid[new_i][new_j] = 2
                        fresh_count -= 1
                        temp.append((new_i, new_j))
            if flag:
                step += 1
            q = temp
        return step if fresh_count == 0 else -1

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                v = self.stack1.pop()
                self.stack2.append(v)
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                v = self.stack1.pop()
                self.stack2.append(v)
            return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0


if __name__ == '__main__':
    s = Solution()
    grid =  [[0,2]]
    print(s.orangesRotting(grid))