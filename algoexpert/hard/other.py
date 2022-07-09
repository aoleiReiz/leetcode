def quickSort(array):
    # Write your code here.
    quick_sort(0, len(array) - 1, array)


def quick_sort(left, right, array):
    if left > right:
        return
    p1, p2 = partition(left, right, array)
    quick_sort(left, p1, array)
    quick_sort(p2, right, array)


def partition(left, right, array):
    e = array[left]
    i = left
    k = left - 1
    j = right
    while i <= j:
        if array[i] < e:
            k += 1
            array[k], array[i] = array[i], array[k]
            i += 1
        elif array[i] == e:
            i += 1
        else:
            array[i], array[j] = array[j], array[i]
            j -= 1
    return k, i


def multiStringSearch(bigString, smallStrings):
    # Write your code here.
    tabu = {}
    for i, c in enumerate(bigString):
        if c == " ":
            continue
        if c not in tabu:
            tabu[c] = []
        tabu[c].append(i)
    ans = []
    for string in smallStrings:
        if string[0] not in tabu:
            ans.append(False)
        else:
            flag = False
            for start_index in tabu[string[0]]:
                if bigString[start_index: start_index + len(string)] == string:
                    ans.append(True)
                    flag = True
                    break
            if not flag:
                ans.append(False)
    return ans


def patternMatcher(pattern, string):
    # Write your code here.
    counter = {
        "x": 0,
        "y": 0
    }
    for c in pattern:
        counter[c] += 1
    start_pattern_char = pattern[0]
    other_pattern_char = "x" if start_pattern_char != "x" else "y"
    for i in range(1, len(string)):
        cur_string_index = i
        cur_pattern_index = 1
        start_char = string[:i]
        char_length_start = i
        if counter[other_pattern_char] > 0 and (len(string) - char_length_start * counter[start_pattern_char]) % \
                counter[other_pattern_char] != 0:
            continue
        if counter[other_pattern_char] == 0 and counter[start_pattern_char] * start_char != string:
            continue
        elif counter[other_pattern_char] == 0 and counter[start_pattern_char] * start_char == string:
            return [start_char, ""] if start_pattern_char == "x" else ["", start_char]

        char_length_other = (len(string) - char_length_start * counter[start_pattern_char]) // counter[
            other_pattern_char]
        other_char = ""
        while cur_string_index < len(string) and cur_pattern_index < len(pattern):
            if pattern[cur_pattern_index] == start_pattern_char:
                if string[cur_string_index: cur_string_index + char_length_start] != start_char:
                    break
                else:
                    cur_string_index += char_length_start
                    cur_pattern_index += 1
            else:
                if other_char == "":
                    other_char = string[cur_string_index: cur_string_index + char_length_other]
                    cur_pattern_index += 1
                    cur_string_index = len(string) if cur_string_index + char_length_other >= len(
                        string) else cur_string_index + char_length_other
                else:
                    if other_char != string[cur_string_index: cur_string_index + char_length_other]:
                        continue
                    else:
                        cur_string_index += char_length_other
                        cur_pattern_index += 1

        if cur_pattern_index == len(pattern) and cur_string_index == len(string):
            return [start_char, other_char] if start_pattern_char == "x" else [other_char, start_char]
    return []


if __name__ == '__main__':
    p = "xxyxxy"
    string = "gogopowerrangergogopowerranger"
    print(patternMatcher(p, string))
