def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    def backtrack(lo, hi, cache):
        if (lo, hi) in cache:
            return cache[(lo, hi)]
        if lo <= 0 and hi <= 0:
            return False
        can_measure = False
        for cup in measuringCups:
            cup_low, cup_high = cup
            if lo <= cup_low and cup_high <= hi:
                can_measure = True
                break
            new_low = max(0, lo - cup_low)
            new_high = max(0, hi - cup_high)
            can_measure = backtrack(new_low, new_high, cache)
            if can_measure:
                break
        cache[(lo, hi)] = can_measure
        return can_measure

    return backtrack(low, high, {})


def ambiguousMeasurements2(measuringCups, low, high):
    def backtrack(lo, hi, cache):
        if (lo, hi) in cache:
            return cache[(lo, hi)]
        if lo > low and hi > high:
            return False
        can_measure = False
        for cup in measuringCups:
            cup_low, cup_high = cup
            if lo + cup_low >= low and hi + cup_high <= high:
                can_measure = True
                break
            can_measure = backtrack(lo + cup_low, hi + cup_high, cache)
            if can_measure:
                break
        cache[(lo, hi)] = can_measure
        return can_measure

    return backtrack(0, 0, {})
