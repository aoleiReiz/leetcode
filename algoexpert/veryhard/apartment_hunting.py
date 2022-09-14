def apartmentHunting(blocks, reqs):
    # Write your code here.
    n = len(blocks)
    idx = -1
    min_distance = float("inf")
    for i in range(n):
        total_dist = 0
        for req in reqs:
            if not blocks[i][req]:
                # go forward
                prev_idx_dist = float("inf")
                j = i - 1
                while j >= 0:
                    if blocks[j][req]:
                        prev_idx_dist = min(prev_idx_dist, i - j)
                        break
                    else:
                        j -= 1
                j = i + 1
                after_idx_dist = float("inf")
                while j < n:
                    if blocks[j][req]:
                        after_idx_dist = min(after_idx_dist, j - i)
                        break
                    else:
                        j += 1
                dist = min(prev_idx_dist, after_idx_dist)
                total_dist = max(dist, total_dist)
        if total_dist < min_distance:
            min_distance = total_dist
            idx = i
    return idx


def apartmentHunting2(blocks, reqs):
    tabu = {}
    for req in reqs:
        left_closest_idxes = [len(blocks)] * len(blocks)
        right_closest_idxes = [len(blocks)] * len(blocks)
        closest_idxes = [len(blocks) + 1] * len(blocks)
        for i in range(len(blocks)):
            if blocks[i][req]:
                left_closest_idxes[i] = i
            elif i > 0:
                left_closest_idxes[i] = left_closest_idxes[i - 1]
        for i in range(len(blocks) - 1, -1, -1):
            if blocks[i][req]:
                right_closest_idxes[i] = i
            elif i < len(blocks) - 1:
                right_closest_idxes[i] = right_closest_idxes[i + 1]

        for i in range(len(blocks)):
            closest_idxes[i] = min(i - left_closest_idxes[i] if left_closest_idxes[i] != len(blocks) else float("inf"),
                                   right_closest_idxes[i] - i if right_closest_idxes[i] != len(blocks) else float("inf"))
        tabu[req] = closest_idxes

    idx = -1
    min_distance = float("inf")
    for i in range(len(blocks)):
        dist = float("-inf")
        for req in reqs:
            dist = max(tabu[req][i], dist)
        if dist < min_distance:
            min_distance = dist
            idx = i
    return idx


data = {
    "blocks": [
        {
            "gym": False,
            "office": True,
            "school": True,
            "store": False
        },
        {
            "gym": True,
            "office": False,
            "school": False,
            "store": False
        },
        {
            "gym": True,
            "office": False,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "office": False,
            "school": True,
            "store": False
        },
        {
            "gym": False,
            "office": False,
            "school": True,
            "store": True
        }
    ],
    "reqs": ["gym", "office", "school", "store"]
}

print(apartmentHunting2(data["blocks"], data["reqs"]))
