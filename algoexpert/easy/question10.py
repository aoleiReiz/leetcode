def minimumWaitingTime(queries):
    # Write your code here.
    totalWaitingTime = 0
    queries = sorted(queries)
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - idx - 1
        totalWaitingTime += queriesLeft * duration
    return totalWaitingTime
