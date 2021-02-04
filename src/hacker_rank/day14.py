class Difference:
    def __init__(self, a):
        self.__elements = a
        self.difference = []

    def computeDifference(self):
        __elements_len = len(self.__elements)
        for i in range(0, __elements_len - 1):
            for j in range(i + 1, len(self.__elements)):
                self.difference.append(abs(self.__elements[j] - self.__elements[i]))

    def maximumDifference(self):
        return max(self.difference)


d = Difference([8, 19, 3, 2, 7])
d.computeDifference()
print(d.difference)
print(d.maximumDifference())
