def isPalindrome(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


def caesarCipherEncryptor(string, key):
    letters = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    letter_2_idx = {c: i for i, c in enumerate(letters)}
    ans = []
    for i, c in enumerate(string):
        idx = (letter_2_idx[c] + key) % 26
        ans.append(letters[idx])
    return "".join(ans)


def runLengthEncoding(string):
    # Write your code here.
    ans = []
    n = len(string)
    cur_c = string[0]
    cur_count = 1
    for i in range(1, n):
        if cur_c == string[i]:
            cur_count += 1
        else:
            ans.append(f"{cur_count}{cur_c}")
            cur_c = string[i]
            cur_count = 1
        if cur_count == 10:
            ans.append(f"{cur_count - 1}{cur_c}")
            cur_count = 1
    ans.append(f"{cur_count}{cur_c}")
    return "".join(ans)


def generateDocument(characters, document):
    character_count = {}
    for c in characters:
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1
    for d in document:
        if d not in character_count:
            return False
        else:
            character_count[d] -= 1
            if character_count[d] < 0:
                return False
    return True


def firstNonRepeatingCharacter(string):
    # Write your code here.
    counter = {}
    for c in string:
        counter[c] = counter.get(c, 0) + 1
    for i,c in enumerate(string):
        if counter[c] == 1:
            return i
    return -1

