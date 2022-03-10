def getNthFib(n):
    # Write your code here.
    prev = 0
    curr = 1
    if n <= 1:
        return n
    for i in range(2, n+1):
        prev, curr = curr, prev + curr
    return curr
