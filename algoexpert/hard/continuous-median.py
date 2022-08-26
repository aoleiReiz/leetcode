class ContinuousMedianHandler:
    def __init__(self):
        # Write your code here.
        self.median = None
        self.data = []

    def insert(self, number):
        # Write your code here.
        self.data.append(number)
        n = len(self.data)
        j = n - 1
        while j > 0:
            if self.data[j - 1] < number:
                self.data[j] = self.data[j - 1]
                j -= 1
            else:
                break
        self.data[j] = number
        self._set_median()

    def _set_median(self):
        n = len(self.data)
        if n % 2 == 1:
            self.median = self.data[n // 2]
        else:
            self.median = (self.data[n // 2] + self.data[n // 2 - 1]) / 2

    def getMedian(self):
        return self.median


c = ContinuousMedianHandler()
c.insert(5)
c.insert(10)
print(c.getMedian())
c.insert(100)
print(c.getMedian())