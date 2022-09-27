def interweavingStrings(one, two, three):
    # Write your code here.
    if len(three) != len(one) + len(two):
        return False
    cache = [[None for _ in range(len(two) + 1)] for _ in range(len(one) + 1)]
    return are_interwoven(one, two, three, 0, 0, cache)


def are_interwoven(one, two, three, i, j, cache):
    print(i, j)
    if cache[i][j] is not None:
        print("---- using cache")
        return cache[i][j]
    print("---- not using cache")
    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]:
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]
    cache[i][j] = False
    print(f"finish {(i,j)}")
    return False

d = {
  "one": "aabcc",
  "two": "dbbca",
  "three": "aadbbbaccc"
}

print(interweavingStrings(d["one"], d["two"], d["three"]))