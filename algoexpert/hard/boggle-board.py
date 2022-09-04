class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word


def boggleBoard(board, words):
    def is_valid_point(i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    def dfs(i, j, s, visited, trie_node):
        if board[i][j] not in trie_node:
            return
        if (i, j) in visited:
            return
        trie_node = trie_node[board[i][j]]
        if "*" in trie_node:
            s.add(trie_node["*"])
        visited.add((i, j))
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, 1],[-1,-1],[1,-1]]
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if is_valid_point(new_i, new_j):
                dfs(new_i, new_j, s, visited, trie_node)
        visited.remove((i, j))

    trie = Trie()
    for word in words:
        trie.add(word)

    ans = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            dfs(i, j, ans, set(), trie.root)
    return ans


board = [
    ["y", "g", "f", "y", "e", "i"],
    ["c", "o", "r", "p", "o", "u"],
    ["j", "u", "z", "s", "e", "l"],
    ["s", "y", "u", "r", "h", "p"],
    ["e", "a", "e", "g", "n", "d"],
    ["h", "e", "l", "s", "a", "t"]
]
words = ["san", "sana", "at", "vomit", "yours", "help", "end", "been", "bed", "danger", "calm", "ok", "chaos",
         "complete", "rear", "going", "storm", "face", "epual", "dangerous"]

print(boggleBoard(board, words))
