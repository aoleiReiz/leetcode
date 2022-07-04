class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def insert_string(self, string):
        cur = self.root
        for c in string:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur[self.end_symbol] = string


def find_string_in_sub_big_string(big_string, start_idx, trie, contained_strings):
    cur = trie.root
    for c in big_string[start_idx:]:
        if c not in cur:
            break
        cur = cur[c]
        if trie.end_symbol in cur:
            contained_strings[cur[trie.end_symbol]] = True


def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    trie = Trie()
    contained_strings = {}
    for string in smallStrings:
        trie.insert_string(string)
    for i in range(len(bigString)):
        find_string_in_sub_big_string(bigString, i, trie, contained_strings)
    return [s in contained_strings for s in smallStrings]
