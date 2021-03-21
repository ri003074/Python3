import re


class Unit:
    def __init__(self, value):
        self.value = value
        pattern_m = re.compile(r"mV|MV|mA|MA")
        pattern_u = re.compile(r"uV|UV|uA|UA")
        pattern_n = re.compile(r"nV|NV|nA|NA")
        if pattern_m.search(self.value):
            self.value = pattern_m.sub("* 10 ** -3", self.value)
        elif pattern_u.search(self.value):
            self.value = pattern_u.sub("* 10 ** -6", self.value)
        elif pattern_n.search(self.value):
            self.value = pattern_n.sub("* 10 ** -9", self.value)

        self.value = eval(self.value)


unit = Unit("10uV")
print(unit.value)
print(type(unit.value))
