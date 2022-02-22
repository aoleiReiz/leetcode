from queue import Queue
from typing import List
from collections import OrderedDict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key=lambda x : x[0]*x[0] + x[1]*x[1])
        return points[:K]

    def man_dist(self, pos1, pos2):
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
    
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        poss = [[i,j]for i in range(R) for j in range(C) if i!=r0 or j !=c0]
        ret = [[r0, c0]]
        poss = [(pos, self.man_dist(pos, [r0, c0]))for pos in poss]
        poss = sorted(poss, key=lambda x : x[1])
        ret2 = [pos[0] for pos in poss]
        return ret + ret2

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        start_indexes = []
        for i in range(n):
            if gas[i] >= cost[i]:
                start_indexes.append(i)
        if not start_indexes:
            return -1

        for i in start_indexes:
            start_index = i
            cur_gas = gas[i]

            while (i + 1) % n != start_index:
                if cur_gas < cost[i]:
                    break
                cur_gas = cur_gas - cost[i] + gas[(i + 1) % n]
                i = (i + 1) % n
            if (i + 1) % n == start_index and cur_gas - cost[i] >= 0:
                return start_index
        return -1

    def countNodes(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        left_count = self.countNodes(root.left)
        right_count = self.countNodes(root.right)

        return left_count + right_count + 1

    def sortString(self, s: str) -> str:
        d = dict()
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        ret = []
        keys = sorted(list(d.keys()))
        i = 0
        while sum(d.values())>0:
            if i % 2 == 0:
                for k in keys:
                    if d[k] > 0:
                        ret.append(k)
                        d[k] -= 1
            else:
                for k in keys[::-1]:
                    if d[k] > 0:
                        ret.append(k)
                        d[k] -= 1
            i+=1
        return "".join(ret)

    def reverseOnlyLetters(self, s: str) -> str:
        c_arr = [i for i in s]
        i = 0
        j = len(c_arr) - 1
        while i < j:
            while i < j and not ('a' <= c_arr[i] <= 'z' or 'A' <= c_arr[i] <= 'Z'):
                i += 1
            while i < j and not ('a' <= c_arr[j] <= 'z' or 'A' <= c_arr[j] <= 'Z'):
                j -= 1
            if i < j:
                tmp = c_arr[i]
                c_arr[i] = c_arr[j]
                c_arr[j] = tmp
                i += 1
                j -= 1

        return "".join(c_arr)


if __name__ == '__main__':
    s = Solution()
    strings = ["ab-cd", "a-bC-dEf-ghIj","Test1ng-Leet=code-Q!"]
    for string in strings:
        print(s.reverseOnlyLetters(string))


