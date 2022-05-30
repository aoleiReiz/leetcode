# Feel free to add new properties and methods to the class.
class MinMaxStack:

    def __init__(self):
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        # Write your code here.
        return self.stack[-1]

    def pop(self):
        # Write your code here.
        if self.stack:
            self.min_max_stack.pop()
            return self.stack.pop()

    def push(self, number):
        # Write your code here.
        if self.min_max_stack:
            new_min_max = {"min": min(self.min_max_stack[-1]["min"], number),
                           "max": max(self.min_max_stack[-1]["max"], number)}
            self.min_max_stack.append(new_min_max)
        else:
            self.min_max_stack.append({"min":number, "max":number})
        self.stack.append(number)

    def getMin(self):
        # Write your code here.
        if self.min_max_stack:
            return self.min_max_stack[-1]["min"]

    def getMax(self):
        # Write your code here.
        if self.min_max_stack:
            return self.min_max_stack[-1]["max"]

